# Loading Package
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import collections

class PickMe:
    def __init__(self,link,keyword,num,repeat):
        self.link = link
#         option=webdriver.ChromeOptions()
#         option.add_argument('headless') # set option
#         self.driver = webdriver.Chrome("./chromedriver",chrome_options=option) # Call Google Chrome with parameters
        self.driver = webdriver.Chrome("./chromedriver")
        self.keyword = keyword
        self.comments = []
        self.check_comments = []
        self.num = int(num)
        if repeat == "True": self.repeat = True
        else : self.repeat = False
    
    def goInstagram(self):
            self.driver.get('https://www.instagram.com')
            sleep(2)

    def login(self):
        user = 'PickMe_ig'
        pw = 'mitfyd-hossit-Pasfu6'
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')

        username.send_keys(user)
        password.send_keys(pw)

        loginBtn = self.driver.find_element_by_css_selector('.L3NKy > div:nth-child(1)')
        loginBtn.click()
        sleep(4)



    def getComment(self):
        self.driver.get(self.link)
        sleep(3)
        while True:
            try:
                target = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span'
                main = self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span')
        #         WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, target)))
                main.click()
                sleep(2)
            except NoSuchElementException:
                break
        comments = self.driver.find_elements_by_css_selector('.C4VMK')
        i = 0
        All_comment= []
        for comment in comments:
            if i == 0:
                i+=1
                continue
#             elif i == 10:
#                 break
            i += 1
#             print('{0:4} -> {1}'.format(i, comment.text))
            All_comment.append(comment.text)
             
        return All_comment
    
    def check_repeat(self):
        if not self.comments:
            print("There are no comments in the post !")
            return
        
        dict_repeat = collections.defaultdict(int)
        for comment in self.comments:
            tmp = comment.split('\n')
            if tmp[1][0] != '@': continue
            tmp_id2 = tmp[1].split(' ')
            id_ = tmp[0] + tmp_id2[0]
            try:
                if dict_repeat[id_] == 0 and tmp_id2[1] == self.keyword:
                    dict_repeat[id_] += 1
                    self.check_comments.append(tmp[0])
                else:
                    continue
            except:
                print(comment)
                
        if self.repeat:
            return
        else:
            tmp_set = set(self.check_comments)
            self.check_comments = list(tmp_set)
            return 
    
    def Pick(self):
        nums = random.sample(range(0, len(self.check_comments)), self.num)
        nums.sort()
        pos = 0
        print("* 恭喜中獎者:")
        for i in range(len(self.check_comments)):
            if nums[pos] == i:
                tmp = self.check_comments[i]
                pos+=1
                print(tmp)
            if pos == len(nums):
                break

