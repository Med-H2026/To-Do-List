import json
from colorama import Fore,Back,Style,init
init()
L=[]
saved = True # track if file already updated and saved

def menu():
    global L
    while True:
        print(Fore.GREEN +'\t 📝 MY TO-DO LIST \n'+Style.RESET_ALL)
        print(Fore.RED + '1.' + Style.RESET_ALL + ' View/Edit Tasks')
        print(Fore.RED + '2.' + Style.RESET_ALL + ' Add Task')
        print(Fore.RED + '3.' + Style.RESET_ALL + ' Mark Task as Done/Not Done')
        print(Fore.RED + '4.' + Style.RESET_ALL + ' Delete Task')
        print(Fore.RED + '5.' + Style.RESET_ALL + ' Save To File')
        print(Fore.RED + '6.' + Style.RESET_ALL + ' Exit \n')
        choice= int(input('Enter your choice:'))
        if choice == 1:
            view_tasks(L)
        elif choice == 2:
            add_task()
        elif choice == 3:
            Mark_task_asDone(L)
        elif choice == 4:
            delete_task(L)
        elif choice == 5:
            save_to_file(L)
        elif choice == 6:
            exit_app(L)
        else:
            choice= int(input('need to choose a number between 1 and 5:'))
            continue


def view_tasks(L):
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    if len(L)> 0:
        print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
        for i,task in enumerate(L, start=1):
            if task['done']:
                print('[✅ ]',Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
            else:
                print('[ ]',Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
        print()
        print('[ ] = not done, [✅ ] = done')
        choice = int(input('press 1 to edit existing task or 2 to mark a task as done or 0 to go back to Menu: '))
        if choice == 0:
            menu()
        elif choice == 1:
            edit_task(L)
        elif choice == 2:
            Mark_task_asDone(L)
        else:
            choice = int(input('Sorry you should press 1 to edit existing task or 0 to go back to Menu: '))
    else:
        print('\n',Fore.RED,'Your To-Do List is empty, Kindly add a new task:',Style.RESET_ALL,'\n')
        menu()

def add_task():
    global saved
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    task= input('Enter new Task: ')    
    L.append({'name':task, 'done':False})
    saved = False
    save_to_file(L)
    print(Fore.GREEN,'Task added successfully!',Style.RESET_ALL)
    choice = int(input('press 0 to go back to Menu or press 1 to add new task:'))
    if choice == 0:
        menu()
    elif choice == 1:
        add_task()
    

def edit_task(L):
    
    while True:
        global saved
        index_task = int(input('Kindly type the task number which you want to edit:'))
        new_msg = input('Please type your new Task:')
        if 0<index_task<=len(L):
            L[index_task-1] = {'name':new_msg, 'done':L[index_task-1]['done']}
            saved = False
            save_to_file(L)
            print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
            for i,task in enumerate(L,start=1):
                if task['done']:
                    print('[✅ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                else:
                    print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
            print()
            print('[ ] = not done, [✅ ] = done')
            choice=int(input('press 1 to edit another task or 0 to go back to Menu: '))
            if choice == 0:
                menu()
            elif choice == 1:
                edit_task(L)
            else:
                choice=int(input('Sorry you should press 1 to edit another task or 0 to go back to Menu: '))

        else:
            print('index out of range, please try again')
            continue

def Mark_task_asDone(L):
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
    for i,task in enumerate(L,start=1):
        if task['done']:
            print('[✅ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
        else:
            print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
    print()
    print('[ ] = not done, [✅ ] = done')
    while True:
        global saved
        choice = int(input('Please enter the number of the task you want to mark as done or press 0 to go back to menu: '))
        if 0<choice<= len(L):
            if task['done'] == False:
                L[choice-1] = {'name':L[choice-1]['name'],'done':True}
                saved = False
                save_to_file(L)
                print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
                for i,task in enumerate(L,start=1):
                    if task['done']:
                        print('[✅ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                    else:
                        print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                print()
                print('[ ] = not done, [✅ ] = done')
            else:
                L[choice-1] = {'name':L[choice-1]['name'],'done':False}
                saved = False
                save_to_file(L)
                print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
                for i,task in enumerate(L,start=1):
                    if task['done']:
                        print('[✅ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                    else:
                        print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                print()
                print('[ ] = not done, [✅ ] = done')
        elif choice == 0:
            menu()
            
        else:
            choice = int(input('index out of range, please try again: '))

def delete_task(L):
    global saved
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    if len(L)> 0:
        print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
        for i,task in enumerate(L,start=1):
            if task['done']:
                print('[✅ ]', Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
            else:
                print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
        print()
        print('[ ] = not done, [✅ ] = done')
    else:
        print(Fore.GREEN,'Your To-Do List is empty, Kindly add a new task:',Style.RESET_ALL,'\n')
        menu()
    while True:
        index_to_del=int(input('Kindly choose the index of the task you want to delete or press 0 to go back to menu:'))
        if index_to_del == 0:
            menu()
        elif 0<index_to_del<=len(L):
            del L[index_to_del-1]
            saved = False
            save_to_file(L)
            if len(L)> 0:
                print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
                for i,task in enumerate(L,start=1):
                    if task['done']:
                        print('[✅ ]', Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
                    else:
                        print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
            print()
            print('[ ] = not done, [✅ ] = done')
            choice = int(input('press 1 to delete another task or 0 to go back to Menu: '))
            if choice == 1:
                delete_task(L)
            else:
                menu()
            break
        else:
            print('index out of range, please choose again!')
            continue
    
def save_to_file(L):
    global saved
    if not saved:
        with open('To-Do-List.json','w',encoding='utf-8') as f:
            json.dump(L,f, indent=4)
        saved = True
    else:
        print('\n',Fore.GREEN,'File already Saved!',Style.RESET_ALL,'\n')
    
def exit_app(L):
    if not saved:
        msg = input('you have unsaved changes, save before exiting? y/n: ')
        if msg.lower() == 'y':
            save_to_file(L)
    print('Goodbye!')
    exit()        

def main():
    menu()

if __name__ == '__main__':
    main()
  