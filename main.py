import yaml
import time
import schedule

import telegram

from datetime import datetime
from selenium import webdriver as wd

def buy_lottery(account_config):
    # open browser
    driver = wd.Edge(executable_path="msedgedriver.exe")

    # login
    login_page = "https://dhlottery.co.kr/user.do?method=login&returnUrl="
    driver.get(login_page)
    driver.implicitly_wait(3)
    id_xpath = "/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[1]"
    pw_xpath = "/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]"
    login_button_xpath = "/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/a"
    driver.find_element('xpath', id_xpath).send_keys(account_config['id'])
    driver.find_element('xpath', pw_xpath).send_keys(account_config['pw'])
    driver.find_element('xpath', login_button_xpath).click()
    time.sleep(3)

    # close pop-up
    windows_list = driver.window_handles
    for i in range(len(windows_list) - 1):
        driver.switch_to.window(windows_list[i + 1])
        driver.close()
    
    # buy lotto645
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(3)
    buy_lotto645_page = "https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40"
    driver.get(buy_lotto645_page)
    driver.switch_to.frame('ifrm_tab')
    driver.find_element('xpath', '//*[@id="num2"]').click() # "자동번호 발급"
    driver.find_element('xpath', '//*[@id="amoundApply"]').send_keys(5) # 구매수량 선택 "5" 
    driver.find_element('xpath', '//*[@id="btnSelectNum"]').click() # "확인"
    driver.find_element('xpath', '//*[@id="btnBuy"]').click() # "구매하기"
    driver.find_element('xpath', '//*[@id="popupLayerConfirm"]/div/div[2]/input[1]').click() # 구매하시겠습니까? "예"

    # buy pension lottery
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(3)
    buy_pension_lottery_page = "https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LP72"
    driver.get(buy_pension_lottery_page)
    driver.switch_to.frame('ifrm_tab')
    driver.find_element('xpath', '//*[@id="lotto720_lottery_wrapper_bg"]/div/div[1]/a').click() # "자동번호"
    driver.find_element('xpath', '//*[@id="lotto720_lottery_wrapper_bg"]/div/div[3]/a').click() # "선택완료"
    driver.find_element('xpath', '//*[@id="frm"]/div/ul[4]/li[5]/a').click() # "구매하기"
    driver.find_element('xpath', '//*[@id="lotto720_popup_confirm"]/div/div[3]/a[1]').click() # 선택한 번호로 구매를 진행합니다 "구매하기"
    time.sleep(5)

    # close browser
    global is_executed
    is_executed = True
    driver.quit()


def send_telegram_message(telegram_config):
    # send telegram message
    bot = telegram.Bot(token=telegram_config['api_token'])
    bot.sendMessage(chat_id=telegram_config['id'] , text="복권 구매 완료")


if __name__ == '__main__':
    global is_executed 
    is_executed = False
    # set config
    with open("./configs/telegram.yaml") as f:
        telegram_config = yaml.load(f, Loader=yaml.FullLoader)
    with open("./configs/account.yaml") as f:
        account_config = yaml.load(f, Loader=yaml.FullLoader)

    # run at trigger time everyweek
    trigger_time = "21:00"
    schedule.every().sunday.at(trigger_time).do(buy_lottery, account_config)
    while True:
        if datetime.now().second == 0:
            run_script = str(schedule.get_jobs())
            print(datetime.now(), run_script[run_script.find('(last run:'):-1])
            schedule.run_pending()
            if is_executed:
                send_telegram_message(telegram_config)
                is_executed = False
            time.sleep(1)
        time.sleep(0.9)