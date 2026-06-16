# 읍·면·대표 동 14개 페이지 집계.
# 이천시는 행정구가 없으므로 읍·면·동을 그대로 대표 페이지로 둔다.
# 세부 법정동(안흥동·갈산동·사음동 등)은 대표 페이지 본문에서 보조 설명한다.
from .areas_g1 import PAGES as _G1
from .areas_g2 import PAGES as _G2

PAGES = _G1 + _G2
