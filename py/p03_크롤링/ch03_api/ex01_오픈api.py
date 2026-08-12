# 오픈 API로 부동산 데이터 크롤링하기
# API 사용하기
# https://www.data.go.kr/
# https://www.reb.or.kr/r-one/portal/openapi/openApiDevPage.do#

import os
import requests
from dotenv import load_dotenv

# 1. 환경변수 로드 및 키 설정
load_dotenv()
serviceKey = os.getenv("REB_SERVICE_KEY")

# 2. API 설정 (복잡한 반복문 없이 딱 1페이지만 요청)
endpoint = "https://www.reb.or.kr/r-one/openapi/SttsApiTbl.do"
params = {
    "KEY": serviceKey,
    "Type": "json",
    "pIndex": "1",
    "pSize": "100",     # 에러가 나지 않는 안전한 크기 설정
    "STATBL_ID": "A_2024_00900"   # ⚠️ 현재 공공데이터포털 가이드북에 적힌 정확한 코드로 교체 필요
}

headers = {"User-Agent": "Mozilla/5.0"}

try:
    print("📡 R-ONE 서버에서 샘플 데이터를 가져오는 중...")
    response = requests.get(endpoint, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    
    # 3. 서버가 돌려준 원본 데이터 그대로 출력
    print("\n[📢 서버 응답 원본 결과]")
    print(response.text)

except Exception as e:
    print(f"❌ 접속 실패: {e}")


""" 
📡 R-ONE 서버에서 샘플 데이터를 가져오는 중...

[📢 서버 응답 원본 결과]
{
    "SttsApiTbl": 
        [   {"head":
                [
                    {"list_total_count":1},
                    {"RESULT": 
                        {"CODE":"INFO-000","MESSAGE":"정상 처리되었습니다."}
                    }
                ]},
            {"row": 
                [{"STATBL_ID":"A_2024_00900","STATBL_NM":"(연) 지역별 지가지수","DTACYCLE_CD":"YY","DTACYCLE_NM":"매년","STAT_ID":"S227720243","TOP_ORG_NM":"한국부동산원","OPEN_STATE":"Y","DATA_START_YY":"1987","DATA_END_YY":"2025","STATBL_IDTFR":null,"STATBL_CMMT":"※조사ㆍ통계문의 : 부동산통계처 토지통계부(053-663-8547,545)","V_ORDER":304001,"RPSTUI_NM":"기준시점 : 2026.01.=100.0"}]}
        ]}
"""