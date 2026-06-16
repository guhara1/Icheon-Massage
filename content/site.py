# 사이트 공통 설정
BASE_URL = "https://icheon-massage.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 읍·면·대표 행정동 14곳 (slug, 한글명) — 내부링크·메뉴 공용
# 이천시는 행정구가 없으므로 읍·면·동을 그대로 대표 페이지로 둔다.
AREAS = [
    ("janghowon-eup-chuljangmassage", "장호원읍"),
    ("bubal-eup-chuljangmassage", "부발읍"),
    ("sindun-myeon-chuljangmassage", "신둔면"),
    ("baeksa-myeon-chuljangmassage", "백사면"),
    ("hobeop-myeon-chuljangmassage", "호법면"),
    ("majang-myeon-chuljangmassage", "마장면"),
    ("daewol-myeon-chuljangmassage", "대월면"),
    ("moga-myeon-chuljangmassage", "모가면"),
    ("seolseong-myeon-chuljangmassage", "설성면"),
    ("yul-myeon-chuljangmassage", "율면"),
    ("changjeon-dong-chuljangmassage", "창전동"),
    ("jeungpo-dong-chuljangmassage", "증포동"),
    ("jungni-dong-chuljangmassage", "중리동"),
    ("gwango-dong-chuljangmassage", "관고동"),
]

# 경강선 역세권 3곳 (slug, 한글명) — 이천역·부발역·신둔도예촌역만 생성
STATIONS = [
    ("icheon-station-chuljangmassage", "이천역"),
    ("bubal-station-chuljangmassage", "부발역"),
    ("sindundoyechon-station-chuljangmassage", "신둔도예촌역"),
]

# 생활권·주요 거점 9곳 (slug, 메뉴 표시명, 카드/제목용 풀네임)
LANDMARKS = [
    ("icheon-terminal-chuljangmassage", "이천터미널", "이천터미널"),
    ("icheon-cityhall-area-chuljangmassage", "이천시청 인근", "이천시청 인근"),
    ("icheon-jungangro-area-chuljangmassage", "이천중앙로 생활권", "이천중앙로 생활권"),
    ("seolbong-park-area-chuljangmassage", "설봉공원 인근", "설봉공원 인근"),
    ("ceramic-art-village-area-chuljangmassage", "이천도자예술마을", "이천도자예술마을"),
    ("sk-hynix-area-chuljangmassage", "SK하이닉스 이천 인근", "SK하이닉스 이천 인근"),
    ("majang-premium-outlet-area-chuljangmassage", "마장프리미엄아울렛 인근", "마장프리미엄아울렛 인근"),
    ("janghowon-area-chuljangmassage", "장호원 생활권", "장호원 생활권"),
    ("icheon-ic-area-chuljangmassage", "이천IC 인근", "이천IC 인근"),
]


def area_url(slug):
    return f"/icheon/{slug}/"


def station_url(slug):
    return f"/icheon/{slug}/"


def landmark_url(slug):
    return f"/icheon/{slug}/"


# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("출장마사지 안내", "/#service", [
        ("서비스 안내", "/#service"),
        ("전지역 방문 가능", "/#coverage"),
        ("예약 전 확인 기준", "/#check"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
    ]),
    ("읍·면·동별 안내", "/#areas", [
        (name, area_url(slug)) for slug, name in AREAS
    ]),
    ("역세권별 안내", "/#stations", [
        (name, station_url(slug)) for slug, name in STATIONS
    ]),
    ("생활권·거점 안내", "/#landmarks", [
        (menu, landmark_url(slug)) for slug, menu, _full in LANDMARKS
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 지역", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 전 준비", "/precautions/#prepare"),
        ("외곽 지역 이동 기준", "/precautions/#outer"),
        ("위생·안전 기준", "/precautions/#hygiene"),
        ("자주 묻는 질문", "/precautions/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
