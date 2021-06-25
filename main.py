import PickMe

link = input("1. IG抽獎連結 : ")
keyword = input("2. 留言關鍵字 : ")
tag = input("3. Tag人數 : ")
num = input("4. 抽獎人數 : ")
repeat = input("5. 是否可重複留言(True/False) : ")
print('\n')
pick_me = PickMe.PickMe( link , keyword , tag , num , repeat)
pick_me.goInstagram()
pick_me.login()
pick_me.comments = pick_me.getComment()
pick_me.check_repeat()
pick_me.Pick()