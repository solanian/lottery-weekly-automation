# 로또복권/연금복권 자동구매 (lottery-weekly-automation)

로또 복권과 연금 복권을 매주 자동 구매하는 스크립트입니다. 편의성을 개선하고 binary로 release를 할 수도 있고 안 할 수도 있습니다.

# environment
- windows >= 10

# pre-installation
- edgebrowser: https://www.microsoft.com/ko-kr/edge
- msedgedriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads
- msedgedrive.exe need to exist in workspace folder (windows)

# requirements
- python >= 3.8
- pyyaml
- selenium
- python-telegram-bot

# how to run
위의 환경들을 세팅한 후에 account.yaml에 동행복권 id와 pw를 입력하고 main.py를 실행하시면 됩니다.

telegram.yaml은 구매후 메세지 전송을 위해서 연결하고 싶은 텔레그램 봇의 id와 api-key를 입력하면 됩니다.(선택) 

자세한 내용은 다음 링크를 참조하세요 https://python-telegram-bot.org/
