import json
from colorama import Fore,Back,Style,init
init()
L=[]
File_updated_if_add = False # track if file already updated and saved
File_updated_if_edit = False # track if file already updated and saved
File_updated_if_del = False # track if file already updated and saved 
def menu():
    global L
    while True:
        print(Fore.GREEN +'\t 📝 MY TO-DO LIST \n'+Style.RESET_ALL)
        print(Fore.RED + '1.' + Style.RESET_ALL + ' View/Edit Tasks')
        print(Fore.RED + '2.' + Style.RESET_ALL + ' Add Task')
        print(Fore.RED + '3.' + Style.RESET_ALL + ' Mark Task as Done')
        print(Fore.RED + '4.' + Style.RESET_ALL + ' Delete Task')
        print(Fore.RED + '5.' + Style.RESET_ALL + ' Save To File')
        print(Fore.RED + '6.' + Style.RESET_ALL + ' Exit \n')
        choice= int(input('Enter your choice:'))
        if choice == 1:
            view_tasks(L)
        elif choice == 2:
            add_task()
        elif choice == 3:
            Mark_task_asDone()
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
        for i,e in enumerate(L,start=1):
            print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , e)
        print()
        print('[ ] = not done, [✅ ] = done')
        choice = int(input('press 1 to edit existing task or 0 to go back to Menu: '))
        if choice == 0:
            menu()
        elif choice == 1:
            edit_task(L)
        else:
            choice = int(input('Sorry you should press 1 to edit existing task or 0 to go back to Menu: '))
    else:
        print('\n',Fore.RED,'Your To-Do List is empty, Kindly add a new task:',Style.RESET_ALL,'\n')
        menu()

def add_task():
    global File_updated_if_add
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    task= input('Enter new Task: ')
    L.append(task)
    save_to_file(L)
    File_updated_if_add = True
    print(Fore.GREEN,'Task added successfully!',Style.RESET_ALL)
    choice = int(input('press 0 to go back to Menu or press 1 to add new task:'))
    if choice == 0:
        menu()
    elif choice == 1:
        add_task()
    

def edit_task(L):
    '''if len(L)>0:
        print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
        for i,e in enumerate(L,start=1):
            print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,e)
        print()
        print('[ ] = not done, [✅ ] = done')
    else:
        print(Fore.GREEN,'Your To-Do List is empty, Kindly add a new task:',Style.RESET_ALL,'\n')
        menu() '''
    while True:
        global File_updated_if_edit
        index_task = int(input('Kindly type the task number which you want to edit:'))
        new_msg = input('Please type your new Task:')
        if 0<index_task<=len(L):
            L[index_task-1] = new_msg
            save_to_file(L)
            File_updated_if_edit = True
            print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
            for i,e in enumerate(L,start=1):
                print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,e)
            print()
            print('[ ] = not done, [✅ ] = done')
            choice=int(input('press 1 to edit another task or 0 to go back to Menu: '))
            if choice == 0:
                menu()
            elif choice == 1:
                edit_task()
            else:
                choice=int(input('Sorry you should press 1 to edit another task or 0 to go back to Menu: '))


        else:
            print('index out of range, please try again')
            continue

def Mark_task_asDone():
    pass

def exit_app(L):
    save_to_file(L)
    exit()

def delete_task(L):
    global File_updated_if_del
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    if len(L)> 0:
        print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
        for i,e in enumerate(L,start=1):
            print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , e)
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
            save_to_file(L)
            File_updated_if_del = True
            if len(L)> 0:
                print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
                for i,e in enumerate(L,start=1):
                    print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , e)
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
    global File_updated
    if not File_updated_if_del or not File_updated_if_add or not File_updated_if_edit:
        with open('To-Do-List.json','w',encoding='utf-8') as f:
            json.dump(L,f, indent=4)
    else:
        print('\n',Fore.GREEN,'File already Saved!',Style.RESET_ALL,'\n')
    

def main():
    menu()

if __name__ == '__main__':
    main()
  