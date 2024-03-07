# -*- coding: utf-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



def start(date,currency_code):
        # 第一步：模拟登录对应的网站
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        boc_url = 'https://www.boc.cn/sourcedb/whpj/'
        browser.get(boc_url)
        #print(browser.title)

        dic = {
            'GBP': '英镑',
            'HKD': '港币',
            'USD': '美元',
            'CHF':'瑞士法郎',
            'DEM':'德国马克',
            'FRF':'法国法郎',
            'SGD':'新加坡元',
            'SEK':'瑞典克朗',
            'DKK':'丹麦克朗',
            'NOK':'挪威克朗',
            'JPY':'日元',
            'EUR':'欧元'
        }

        # 在网页中设置起始时间
        browser.find_element(By.XPATH,'//*[@id="historysearchform"]/div/table/tbody/tr/td[2]/div/input').clear()
        browser.find_element(By.XPATH,'//*[@id="historysearchform"]/div/table/tbody/tr/td[2]/div/input').send_keys(
            date)

        # 在网页中设置外汇类型
        S = Select(browser.find_element(By.NAME,'pjname')).select_by_visible_text(dic[currency_code])

        # 进行查询
        browser.find_element(By.XPATH,'//*[@id="historysearchform"]/div/table/tbody/tr/td[7]').click()
        # ['货币名称', '现汇买入价', '现钞买入价', '现汇卖出价', '现钞卖出价', '中行折算价', '发布时间']
        result=browser.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text

        print(result)

        with open('result.txt', 'w') as f:
            f.write(result)
            f.close()


if __name__=='__main__':
    date = sys.argv[1]
    currency_code = sys.argv[2]
    start(date,currency_code)







