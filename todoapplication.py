users = []

todos = []

logged_in_user = None

from os import system
system("cls")

def signup():
    system("cls")
    print("Signup Screen".center(50,"*"))
    visitor = {'Uid': len(users)+1,'Name': input('Enter your name: '),'Username': input('Enter username: '),'Password': input('Enter password: ')}
      
     # check if username is unique
    all_users_username = [usr['Username'] for usr in users]
    if visitor['Username'] in all_users_username:
        print('Username is already taken, try different')
        signup()
    else:
        print('User is registered!')
        users.append(visitor)

#signup()
#signup()
#print(users)
        

def login():
    system("cls")
    global logged_in_user
    print("Login Screen".center(50,"*"))
    username = input('Enter username (case sensitive): ')
    
    user_dict = None
    for usr in users:
        if usr['Username'] == username:
           user_dict = usr
           break
    if not user_dict:
           print('Username is incorrect')
           login()
    
    password= input('Enter password: ')
    if user_dict:
       if password == user_dict['Password']:
          print('Login is successful')
          logged_in_user = user_dict['Uid']
       else:
          print('password is incorrect')
          login()

#signup()
#login()
#print(logged_in_user)
               


def addtodo():
        system("cls")
        print("Addtodo Screen".center(50,"*"))
        if logged_in_user:
                 task = {'tid':len(todos)+1,
                         'Uid':logged_in_user,
                         'title':input("Enter title: "),
                         'status':input("Enter status: "),
                         'Deadline':input("Enter deadline: ")
                        }
                 todos.append(task)
                 ch = input('ADD MORE TASK? : ').lower()[0]
                 if ch == 'y':
                       addtodo()
        else:
              print('Please log in')
              login()
              addtodo()

'''signup()
login()
addtodo()
print(todos)'''

def showtodo():
        system("cls")
        print("Showtodo Screen".center(50,"*"))
        if logged_in_user:
            if todos:
               for usr in todos:
                 if usr['Uid'] == logged_in_user:
                         print('TASK ID:',usr['tid'])
                         print('TASK TITLE:',usr['title'])
                         print('TASK STATUS:',usr['status'])
                         print('TASK DEADLINE:',usr['Deadline'])
                         print()
            else:
               print('Add some tasks')
               addtodo()
                
           
        else:
             print('Please log in')
             login()
             showtodo()
               

def updatetodo():
             system("cls")
             global todos
             print("Updatetodo Screen".center(50,"*"))
             if logged_in_user:
                     
                     task_id = int(input('Enter task id: '))
                     print()
                     update = {1:("Update Title",'title'),2:("Update Status","status"),3:("Update Deadline","Deadline")}

                     for num,option in update.items():
                                   print(num,option[0],sep="---->")
                     print()
                     ch = int(input('ENTER OPTION: '))
  
                     if todos:
                       for usr in todos:
                          if usr['Uid'] == logged_in_user and usr['tid']==task_id:
                               if ch in update:
                                   usr[update[ch][-1]] = input('New Value : ')
                              
                       updates = input('Want to update something else? ').lower()[-1]
                       if updates == 'y':
                              updatetodo()
                     
                     else:
                          print('ADD some tasks')
                          addtodo()
             else:
                print('Please log in')
                login()
                updatetodo()
                     
                    
                                   
                                     
def deletetodo():
              system("cls")
              global todos
              print("deletetodo Screen".center(50,"*"))
              if logged_in_user:
                    if todos:
                         task = int(input('Enter Task ID to delete: '))
                         for i in range(len(todos)):
                              if todos[i]['tid'] == task:
                                     del todos[i]
                                     break
                         
                                     
                                     
                    else:
                        print('ADD SOME TASKS!')
                        addtodo()
              else:
                print('Please log in')
                login()
                deletetodo()
                   
                               
def exit():
     global logged_in_user
     logged_in_user = None
     print("Logged out")
 

options = {1:("SIGN-UP",signup),2:("LOGIN",login),3:("ADD TODO",addtodo),4:("SHOW TODO",showtodo),5:("UPDATE TODO",updatetodo),6:("DELETE TODO",deletetodo),7:("EXIT",exit)}

while True:
 print("Menu Screen".center(50,"*"))
 for num,option in options.items():
        print(num,option[0],sep="---->")

 ch = int(input('ENTER OPTION: '))
 if ch in options:
    options[ch][-1]()
 else:
    print('INCORRECT OPTION')
