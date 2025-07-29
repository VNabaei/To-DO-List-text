# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 15:00:47 2025

@author: HP
"""
#برای گرفتن نام ایجاد کننده یا نام ویرایشگز
import getpass 
from datetime import datetime



class To_Do_List:
    list_counter = 0
    
    # --- constructor 
    def __init__ (self,Title_Name : str):
        
        # -- the id format :
        #TLD-XXXX-TLD-YYYY-Date Time.
        #TLD : To Do List ,
        #TSK : task,
        #XXXX :counter of n-th todolist x in range (0,8),
        #YYYY: counter of m-th Task Y in range (0,8).
        
        self.TLDid  = f"TDL-{To_Do_List.list_counter:08d}"    # It's manual for now, I'll fix it later.😅
        
        self.tasks_counter = 0 # for create the TSK id.
        self.tasks= [] #put the tasks of TLD here.
        self.Title_Name = Title_Name

        self.history = []
        # history format = {action : ,idTask : , dateAction: , who: }
        self.History("new Todo list",self.TLDid) 
        
        
        To_Do_List.list_counter += 1 #done !
        
        
        
    # ---- the functions:    
    def History (self,action , idTask ):
        self.history.append({
            "action": action,
            "IDTask/target": idTask,
            "date time": datetime.now() ,
            "performed_by ":getpass.getuser()
            })
        
    # ---- for the tasks : (composition)
    def add_task(self,title_Name,title : str):
        
        # -- id :
        self.tasks_counter +=1
        
        newTask = Task(self.tasks_counter,title_Name,title)
        self.tasks.append(newTask)
        
        id = self.TDLid + "-" + newTask.TSKid
        self.History("new task",id) 



class Task :
    
    def __init__ (self,tasks_counter: int,title): #to fix bug we defin the ddline function .
        # -- id :
        self.TSKid = f"TSK-{tasks_counter:08d}"
        self.title = title
        self.DDline = self.add_DDLine()
        self.subtask = []
        self.info = self.add_info()
        self.status = "created"
        
        
        self.tasks.append({
            "title" : self.title ,
            "DDline" : self.DDline ,
            "subtask" : self.subtask,
            "info" : self.info,
            "Status" : self.status,
            "creator" : getpass.getuser()
            })

  
    def add_DDLine(self ):
        while True:
            try :
    
                user_input = input("input the day : (ex: 2025-07-29): ")
                if not user_input.strip():
                    return datetime().today().date() #ممکن است کاربر اریخ وارد نکند برای همین به صورت  پیش فرض تاریخ امروز را میزنم
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
    
    
    def search_task(self):
        pass
    
    def remove_task(self):
        
        #should call the search_task function
        pass
    
    def edit_task(self):
        #should call the search_task function
        pass
    
    def Status (self)  :
        pass
        # وضعیت تسک را چک کن اگر اتمام نرسیده بود و فعال بوذ :
        #تاریخ سیستم را با تاریخ ددلاین محاسبه کن اگر از تاریخ گذشته بود :
            #وضعیت تسک را بزن تاخیر خورده
            # و گرنه هیچی
        
        