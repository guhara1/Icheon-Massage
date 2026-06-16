#!/usr/bin/env python3
"""구글 Indexing API 색인 요청 (선택).

중요 — 구글 공식 정책:
  • 구글은 IndexNow에 참여하지 않습니다.
  • Indexing API는 공식적으로 JobPosting/BroadcastEvent 구조화 데이터 페이지만
    지원 대상으로 명시합니다. 일반 지역 안내 페이지의 가장 정석적인 색인 경로는
    (1) Search Console에 sitemap.xml 제출, (2) URL 검사 도구로 색인 요청 입니다.
  • 그럼에도 이 스크립트는 운영자 판단 하에 Indexing API로 URL 갱신을 통보할 수
    있도록 준비해 둔 보조 도구입니다. 정책 변동 가능성을 인지하고 사용하세요.

준비물:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급 → 파일로 저장
  3) Search Console 속성에 해당 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python3 tools/google_indexing.py                # sitemap.xml 전체
  python3 tools/google_indexing.py URL [URL ...]  # 지정 URL만
"""
import os
import re
import sys

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def main(urls):
    try:
        import google.auth.transport.requests
        from google.oauth2 import service_account
    except ImportError:
        sys.exit("google-auth 가 필요합니다:  pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")

    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    session = google.auth.transport.requests.AuthorizedSession(creds)

    for url in urls:
        body = {"url": url, "type": "URL_UPDATED"}
        r = session.post(ENDPOINT, json=body, timeout=30)
        print(f"[{r.status_code}] {url}")


if __name__ == "__main__":
    main(sys.argv[1:] or sitemap_urls())
