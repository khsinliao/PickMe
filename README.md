# PickMe : Draw from a Instagram post

###### tags: `IG抽獎神器` `抽獎神器` `@update_foodiary`
![](https://img.shields.io/static/v1?label=MacOS&message=11.2.1&color=red) ![](https://img.shields.io/static/v1?label=python&message=3.8&color=blue) ![](https://img.shields.io/static/v1?label=Selenium&message=3.141.0&color=orange) 


## Introduction ⭐
> This repo is for Instagram user to draw the specific comments in the post.

## Prerequisite 💡
### Full Install (ok to run)
- [x] Python 3.8
- [x] Selenium
- [x] Webdriver 

* How to install Selenium ?
```
pip install selenium
```
* How to install Webdriver ?
  + [Chrome](https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19/) (Suggest)
  + [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
  + [Firefox](https://github.com/mozilla/geckodriver/releases)
  + [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## How to run 🤞🏻

* Clone this repo 🔥
```
git clone https://github.com/khsinliao/PickMe.git
cd PickMe
```

* Run the exec file of chromedriver (Webdriver) 💥
```
# If you are MacOS user , you may encounter the system's prohibition to open the file since it is not authenticated by Apple Store.

> Hold the 'control' key and click it to force open.
```

* Run the script 🌟
```
python main.py
```
* Input the post's information
```
1. IG抽獎連結 : 
2. 留言關鍵字 :
3. 抽獎人數 :
4. 是否可重複留言(True/False) :
```
* Example ☀️
![](https://i.imgur.com/sRwy1zl.png)


## Future Work 🥳

- [ ] Propose the webpage version
- [ ] Decrease the time complexity
- [ ] Try PhantomJS or other headless webdriver
- [ ] Develop Facebook and Youtube ver.
