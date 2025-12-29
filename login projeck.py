import time
All_user_password=[]
user_name=0
def readfile():
 with open("data.txt",'r') as f:#read password in the file
     password_list=[]
     for text in f:
         # 在這檢查
         password_list.append(text.strip().split(','))#把空格拿掉和轉換成list
     #print(password_list)
     for one_list in password_list:
         try:
            All_user_password.append({one_list[0] : {one_list[1] : one_list[2]}})#if it can't found or it not enough it will error
         except :
             print('something wrong')
     print(All_user_password)


def login():#輸路帳號
#這個部分應該要改一點 1.讓他重新讀 2. 如填錯密碼要這麼辦

    login_user_name=input('enter username :')
    user_name=login_user_name
    time.sleep(1)
    login_password=input('enter password : ')
    time.sleep(1)
    for small_data in  All_user_password:#!
        print(small_data)
        if login_user_name in small_data :
         print('user name found')

         if login_password == small_data [login_user_name]['password']: #用這個來尋找密碼
            print('login successful ')
            break


        else :
            print('try agin')
            time.sleep(1)
            return login()
    print('coming manu')
    return manu()





def sign_up():#做一個創招新帳號
    user_name=input("pleas enter your username :")
    time.sleep(1)
    password=input('pleas enter your password :')
    time.sleep(1)
    Make_sure_password=input('pleas confirm your password :')
    time.sleep(1)
    while Make_sure_password != password :#確定密碼是否像第一個密碼一樣
     print('your confirm password is wrong pleas make sure your password')
     Make_sure_password=input('pleas confirm your password : ')#重複一次
     time.sleep(1)


    with open('data.txt','a') as f:#open the file to write
     f.write(f'{user_name},password,{password}\n')#加祿新帳號
    readfile()
    print('your new account is successful')
    time.sleep(1)
    print('pleas login your account')
    time.sleep(1)

    return login()#開始輸路帳號


def manu():#進路裡面

    print('\n')
    print('hi')

    print(f"username {user_name}")
    time.sleep(0.5)
    print('manu')

readfile()
#login()

# print("你好歡迎來到login modeal ")
# print('login \n\nsign up')
#
# choice = input('\n輸路你的選擇：') #make a choice to choose
# time.sleep(0.5)
#
# if choice.strip().upper()== 'LOGIN': # if choose login come to login zone
#
#     print("login Zone \n")
#     time.sleep(0.5)
#     login()
# elif choice.strip().upper()=='SIGNUP': # if choose sighup come to sighup zone
#     print('sign up zone\n')
#     time.sleep(0.5)
#     sign_up()
# else: print('can"t found')
#
