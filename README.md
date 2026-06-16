# 간다GO — 이천 출장마사지·홈타이 지역 SEO 사이트

경기도 이천시에서 방문형 마사지(출장마사지)·홈타이를 찾는 사용자가
본인 위치에 맞는 지역 정보를 쉽게 확인할 수 있도록 만든 정적 지역 SEO 사이트입니다.
이천시는 **행정구가 없는 도시**이므로 읍·면·대표 동을 그대로 대표 페이지로 둡니다.

- **상호:** 간다GO
- **예약전화:** 0508-202-4719
- **핵심 키워드:** 출장마사지 / **보조:** 홈타이
- **지역 키워드:** 이천 출장마사지, 이천시 출장마사지, 이천 홈타이

## 구조 (총 32페이지)

```
메인 1
읍·면·대표 동 14   (장호원읍·부발읍·신둔면·백사면·호법면·마장면·대월면·
                    모가면·설성면·율면·창전동·증포동·중리동·관고동)
경강선 역세권 3    (이천역·부발역·신둔도예촌역)
생활권·주요 거점 9 (이천터미널·이천시청 인근·이천중앙로 생활권·설봉공원 인근·
                    이천도자예술마을·SK하이닉스 이천 인근·마장프리미엄아울렛 인근·
                    장호원 생활권·이천IC 인근)
안내 페이지 5      (예약안내·이용 전 확인사항·홈타이 이용 가이드·
                    개인정보처리방침·고객센터)
```

세부 법정동은 단독 페이지로 만들지 않고 대표 페이지 본문에서 보조 설명합니다.
- 안흥동·갈산동·송정동 → 증포동 페이지
- 사음동·도자예술마을 → 신둔면 페이지
- 율현동·진리동 → 중리동·이천역 생활권
- 부발역은 경강선·중부내륙선을 한 페이지에서 함께 안내(노선별 분리 없음)
- 감곡장호원역은 행정구역상 이천시 역이 아니므로 단독 페이지 없음

## URL 규칙

| 구분 | 경로 |
|------|------|
| 메인 | `/` |
| 읍·면·동 | `/icheon/<slug>-chuljangmassage/` |
| 역세권 | `/icheon/<station>-station-chuljangmassage/` |
| 생활권·거점 | `/icheon/<landmark>-area-chuljangmassage/` |

> 메인페이지는 배포 도메인 루트(`/`)에 위치합니다. 워드프레스 슬러그
> `/icheon-chuljangmassage/`로 운영하려면 해당 경로로 리다이렉트하세요.

## 빌드

```bash
python3 build.py
```

`content/` 패키지의 페이지 정의를 읽어 각 경로에 `index.html`을 생성하고
`sitemap.xml`, `robots.txt`, `.nojekyll`을 갱신합니다.

- 본문 텍스트 2,000자 미만 페이지는 자동으로 `noindex` 처리됩니다.
- 모든 페이지에 `WebPage`·`BreadcrumbList` 구조화 데이터가 자동 삽입되고,
  메인에는 `Organization`·`FAQPage`가 추가됩니다.
- 오프라인 매장 주소가 없으므로 `LocalBusiness` 스키마는 사용하지 않습니다.

## 배포 전 설정

- `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경한 뒤 `python3 build.py` 재실행.

## 색인(인덱싱) 빠르게 하기

빌드(`python3 build.py`)는 색인용 파일을 자동 생성합니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | `<lastmod>` 포함. Search Console·네이버 서치어드바이저에 제출 |
| `feed.xml` | RSS 2.0 보조 피드(콘텐츠 발견 보조). robots.txt에 함께 명시 |
| `robots.txt` | 모든 봇 허용 + sitemap·feed 위치 안내 |
| `<KEY>.txt` | IndexNow 키 파일(`https://도메인/<KEY>.txt`로 검증) |

### 1) IndexNow — 빙·네이버·얀덱스 즉시 통보 (구글 미참여)

```bash
python3 tools/indexnow.py                # sitemap 전체 제출
python3 tools/indexnow.py https://icheon-massage.pages.dev/icheon/...   # 특정 글만
```

- 키 파일이 도메인에 배포된 뒤에 실행해야 합니다(배포 후 최초 1회 수동 실행 권장).
- 이후에는 `.github/workflows/indexnow.yml` 이 **푸시될 때마다 자동 제출**합니다.
  Cloudflare Pages 배포 브랜치에 맞춰 워크플로의 `branches:` 를 조정하세요.

### 2) 구글 — IndexNow 미지원이므로 별도 경로

- **정석:** Search Console에 `sitemap.xml` 제출 + URL 검사 도구로 색인 요청.
- **선택:** `tools/google_indexing.py` (서비스 계정 필요). 구글 Indexing API는 공식적으로
  JobPosting/BroadcastEvent 페이지만 지원 대상으로 명시하므로, 일반 페이지는 위 정석 경로를 우선하세요.

> 참고: 구글·빙의 익명 **sitemap ping 엔드포인트는 2023년 폐지**되었습니다.
> 따라서 sitemap ping 대신 Search Console/서치어드바이저 제출 + IndexNow 조합을 사용합니다.

### 3) 검색엔진 등록(최초 1회)

- 네이버 서치어드바이저: 사이트 등록 → 소유확인(메인 `naver-site-verification` 메타 적용됨) → `sitemap.xml`·`feed.xml` 제출.
- 구글 Search Console: 속성 등록 → `sitemap.xml` 제출.

## 디렉터리

```
build.py            빌드 스크립트
content/            페이지 정의 (site, main, areas, stations, landmarks, info, pricing)
assets/             style.css, nav.js, 파비콘/OG 이미지
tools/              indexnow.py, google_indexing.py (색인 통보 스크립트)
.github/workflows/  indexnow.yml (푸시 시 자동 IndexNow 제출)
```
