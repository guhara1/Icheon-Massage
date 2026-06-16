# 전체 페이지 목록 집계
from . import main, areas, stations, landmarks, info

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + landmarks.PAGES
    + info.PAGES
)
