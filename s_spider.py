import json
import codecs
from spider import login4cookies
from requests import Session
from selenium import webdriver

DRIVER_PATH = "./chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)

def index():
    #首次请求，让selenium 知道自己在哪个域
    driver.get('https://leetcode-cn.com')
    #获取cookies
    cookies = login4cookies()
    print(cookies)
    questions={}
    for cookie in cookies:
        #提取如下两个cookie 字段，只有这俩有用
        if cookie.name == 'csrftoken' or cookie.name=='LEETCODE_SESSION':
            questions[cookie.name] = cookie.value
    #webdriver 添加cookie
    for name,value in questions.items():
        driver.add_cookie({
            "domain": '.leetcode-cn.com',
            "name": name,
            "value": value,
            "path": '/',
            "expire":None
        })
    #带cookie 再次请求
    url=input("请输入需要爬取的题库url：\n")
    driver.get(url)
    questions = {}
    #开始爬题目
    #这个循环爬取中文标题和题目链接，存入questions 字典
    while True:
        tbody=driver.find_element_by_tag_name("tbody")
        q_list = tbody.find_elements_by_tag_name('tr')
        for q in q_list:
            print(q)
            td = q.find_elements_by_tag_name('td')
            if td[0].get_attribute("value") == 'ac':
                question = td[2].find_element_by_tag_name('a')
                questions[question.text] = question.get_attribute('href')
        print(questions)
        try:
            elem = driver.find_element_by_class_name('reactable-next-page')
            elem.click()
        except:
            break
    
    with codecs.open('data.json', 'a+', 'utf-8') as f:
        #从questions 中取出链接
        for title, link in questions.items():
            q = {}
            q['title'] = title
            q['link'] = link
            #请求链接，获取题目内容
            driver.get(link)
            content = driver.find_element_by_class_name("notranslate").find_elements_by_tag_name("p")
            text=''
            for t in content:
                text += t.text
            q['content'] = text
            print(q['content'])
            #请求提交列表
            driver.get(link + '/submissions/')
            sub_list = driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
            for sub in sub_list:
                #检查提交列表的该行是否为 “通过”
                check = sub.find_element_by_tag_name('a')
                if check.text == "通过":
                    check.click()
                    #因为点击通过会打开一个新页面，所以需要将webdriver切换一下

                   
                    driver.switch_to.window(driver.window_handles[1])
                    code = driver.find_elements_by_class_name("ace_line")
                    #获取通过的代码
                    while code == []:
                        code = driver.find_elements_by_class_name("ace_line")
                    t = ''
                    for text in code:
                        t += text.text + '\n'
                    q['code'] = t
                    driver.close()
                    driver.switch_to_window(driver.window_handles[0])
                    print(q['code'])
                    break              
            f.write(json.dumps(q,ensure_ascii=False))
            
    driver.quit()
index()
