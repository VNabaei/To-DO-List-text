# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 15:00:47 2025

@author: HP
"""
#برای گرفتن نام ایجاد کننده یا نام ویرایشگز
import getpass 
from datetime import datetime
import os


'''
 اینا رو می نویسم یادم نشه.
 می خوام جنس تسک ها رو دیکشنری بگذارم و با هی مشخص شن
 خوبه ؟ البته چون یونیکه. البته اینم هست که با عنوان باشه بهتره
 ولی همین آیدی بهتره
 پس دیکشنری میشازم
 '''



class To_Do_List:
    list_counter = 0
    
    # --- constructor 
    def __init__ (self,List_Title : str):
        
        # -- the id format :
        #TLD-XXXX-TLD-YYYY-Date Time.
        #TLD : To Do List ,
        #TSK : task,
        #XXXXXXXX :counter of n-th todolist x in range (0,8),
        #YYYYYYYY: counter of m-th Task Y in range (0,8).
        
        self.TLDid  = f"TDL-{To_Do_List.list_counter:08d}"    # It's manual for now, I'll fix it later.😅
        self.TotalId = creat_TotalId(self, "TSK-00000000")
        
        self.tasks_counter = 0 # for create the TSK id.
        self.tasks= {} #put the tasks of TLD here.
        self.List_Title = List_Title

        self.history = []
        # history format = {action : ,idTask : , dateAction: , who: }
        History("new Todo list",self.TLDid) 
        
        
        To_Do_List.list_counter += 1 #done !
        
        
        
    # ---- for the tasks : (composition)
    def add_task(self,title : str):
        '''
        this function add the task in todo list

        Parameters
        ----------
        List_Title :  str
            the to do list title name.
        title : str
            the task title .

        Returns
        -------
        None.

        '''
        
        # -- id :
        self.tasks_counter +=1
        
        newTask = Task(self.tasks_counter,self.List_Title,title)
        self.tasks[newTask.TSKid] = newTask.TSK2Dic()
        
        id = creat_TotalId(self, newTask)
        
        
        History(self,"new task",id) 


    def simple_search_task(self, target):
        '''
        search the target in title of task
        
        Parameters
        ----------
        target :  str
            
        Returns
        -------
        result of search.

        '''
        results = []
        for task in self.tasks :
            if target.upper() in task["title"].upper() :#نمیدونم استفاد از upper بهتره یا lower
                results.append(task)
                
            if results: #not null
                print (f"{len(results)} result found ")
                counter = 0
                for res in results :
                    counter +=1
                    print (f" {counter}\n")
                
            else: 
                print (f"{target} not found")
                
        return results
 
        
    def remove_task(self,target :str): # این عملیات مستقیم روی list انجام می شود
        tasks = self.tasks["title"]
        for t in tasks :
            if target.upper() in t.upper():
                self.tasks.remove(t)
                print (f"{target} removed")
                return
            else :
                print (f"{target} not found")
        
        
    
    
    def edit_task(self):
        #should call the search_task function
        pass
  
    

class Task :
    
    def __init__ (self,tasks_counter: int,List_Title,title): #to fix bug we defin the ddline function .
        # -- id :
        self.TSKid = f"TSK-{tasks_counter:08d}"
        self.title = title
        self.DDline = self.add_DDLine()
        self.subtask = [] # در حال حاضر پلنی براش دارم ولی نمی نویسم 😅
        self.info = self.add_info()
        self.status = "created"
        self.ToDoList_Title = List_Title
        self.Creator = Get_User()
        self.Created_Time = datetime.today()
        
        
    # برای اینکه جنس تسک ها دیکشنری باشه :
    def  TSK2Dic (self):
        return  {
                "title" : self.title ,
                "ToDoList_Title" :self.ToDoList_Title, 
                "DDline" : self.DDline ,
                "subtask" : self.subtask,
                "info" : self.info,
                "status" : self.status,
                "creator" : self.Creator,
                "Created_at" : self.Created_Time
                }
  
    def add_DDLine(self ):
        while True:
            try :
    
                user_input = input("input the day : (ex: 2025-07-29): ")
                if not user_input.strip():
                    return datetime.today().date() #ممکن است کاربر اریخ وارد نکند برای همین به صورت  پیش فرض تاریخ امروز را میزنم
                user_date = datetime.strptime(user_input, "%Y-%m-%d").date()
                        
                return user_date
        
            except ValueError :
                print ("Your input does not match the required format (year-month-day). Please enter it again : ")
    
        
    def add_info(self):
        print ("در صورت تمایل توضیحات را وارد کنید.")
        info = input("info :\n ")
        return info
     
    '''
    چون جزئیات زیاد داره فعلا اینو بیخیال میشیم
    def add_subtask(self):
        n = input("how many subTask you want to add : ")
        for i in n :
            self.subtask.append(input(f"please inter the {i}-th subTask :  "))
'''     
    
    
   
    
  
    def Status (self)  :
        pass
        # وضعیت تسک را چک کن اگر اتمام نرسیده بود و فعال بوذ :
        #تاریخ سیستم را با تاریخ ددلاین محاسبه کن اگر از تاریخ گذشته بود :
            #وضعیت تسک را بزن تاخیر خورده
            # و گرنه هیچی
    
    # str for show function    
    def __str__ (self):
        return f'title : {self.title} * ToDoList_Title : {self.ToDoList_Title} * info : {self.info} * status : {self.status}'
            
    def Show_Task(self):
        print(self.__str__())
        
# ---- the functions:    
def History (item ,action , idTask ):
    '''
    the function that creat history from action to history array.

    Parameters
    ----------
    item : 
        Task or to do list.
    action : str
        in every function overwriting.
    idTask : str
        Total Id from TDL and TSK.

    Returns
    -------
    None.

    '''
    item.history.append({
               "action": action,
               "IDTask/target": idTask,
               "date time": datetime.now() ,
               "performed_by ":Get_User()
               })   
    
def creat_TotalId(TDL_item , TSK_item):
    '''
    this function creat total id

    Parameters
    ----------
    TDL_item :  To_Do_List
        
    TSK_item :  Task

    Returns
    -------
    TotalId :  str
        DESCRIPTION.

    '''
    TotalId = TDL_item.TDLid + "-" + TSK_item.TSKid
    return TotalId
    

def Get_User():
    try:
        user = getpass.getuser()
        return user
    except Exception:
        return "Unknown"





# D:\MyJob\to_do_list>ssh-keygen -t rsa -b 4096 -C "v.nabaee@gmail.com"
# Generating public/private rsa key pair.
# Enter file in which to save the key (C:\Users\HP/.ssh/id_rsa):
# C:\Users\HP/.ssh/id_rsa already exists.
# Overwrite (y/n)? y
# Enter passphrase (empty for no passphrase):
# Enter same passphrase again:
# Your identification has been saved in C:\Users\HP/.ssh/id_rsa
# Your public key has been saved in C:\Users\HP/.ssh/id_rsa.pub
# The key fingerprint is:
# SHA256:qxrFX0w87dcx5VopEwtq221knRFQH4d5LroKsrzS7DQ v.nabaee@gmail.com
# The key's randomart image is:
# +---[RSA 4096]----+
# |           . ooB+|
# |         .... *.X|
# |         o+ .* O+|
# |     .  .ooo+ +++|
# |      o S.o..+o..|
# |     . . o  o.   |
# |    .oE +    .   |
# |    .+o= .  .    |
# |    .+*.  ..     |
# +----[SHA256]-----+
