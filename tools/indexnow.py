#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스.

IndexNow 프로토콜은 한 곳에 제출하면 참여 검색엔진이 변경 정보를 공유합니다.
신뢰성을 위해 빙·네이버·얀덱스 엔드포인트에 모두 제출합니다.
구글은 IndexNow에 참여하지 않으므로 별도 처리(google_indexing.py / Search Console)가 필요합니다.

사용법:
  python3 tools/indexnow.py                # sitemap.xml 의 모든 URL 제출
  python3 tools/indexnow.py URL [URL ...]  # 지정한 URL만 제출(글 새로 올릴 때)

키 파일은 빌드 시 /{KEY}.txt 로 배포되어 있어야 합니다(build.py가 생성).
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE)
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://yandex.com/indexnow",
]


def sitemap_urls():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")

    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"[{resp.status}] {ep}")
        except urllib.error.HTTPError as e:
            # 200/202 외 코드도 본문에 사유가 담겨 있어 함께 출력
            print(f"[{e.code}] {ep} — {e.read().decode('utf-8', 'ignore')[:200]}")
        except Exception as e:  # noqa: BLE001
            print(f"[ERR] {ep} — {e}")


if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        print("제출할 URL이 없습니다.")
        sys.exit(1)
    print(f"IndexNow 제출: {len(urls)}개 URL → {HOST}")
    submit(urls)
