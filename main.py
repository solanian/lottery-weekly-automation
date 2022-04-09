from pathlib import Path

import yaml
import telegram

from selenium import webdriver


if __name__ == '__main__':
    fname = Path('config.yaml')
    with open(fname) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        

    chrome_options = webdriver.ChromeOptions()
    
    # open lottery homepage
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url='https://dhlottery.co.kr/user.do?method=login&returnUrl=')

    # log in
    driver.find_element_by_xpath('/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[1]').send_keys(config['id'])
    driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]').send_keys(config['pw'])
    driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()
    
    
    # select lottery 645
    driver.get(url='https://dhlottery.co.kr/gameInfo.do?method=buyLotto&wiselog=C_A_1_3')
    driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/div[1]/div[3]/a[3]').click()
    # driver.find_element_by_xpath('//*[@id="gnb"]/ul/li[1]/div/ul/li[1]/a').click() 