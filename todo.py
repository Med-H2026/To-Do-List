from colorama import Fore,Back,Style,init
init()
L=[]
def menu():
    global L
    while True:
        print(Fore.RED +'\t 📝 MY TO-DO LIST \n'+Style.RESET_ALL)
        print(Fore.RED + '1.' + Style.RESET_ALL + ' View Tasks')
        print(Fore.RED + '2.' + Style.RESET_ALL + ' Add Task')
        print(Fore.RED + '3.' + Style.RESET_ALL + ' Mark Task as Done')
        print(Fore.RED + '4.' + Style.RESET_ALL + ' Delete Task')
        print(Fore.RED + '5.' + Style.RESET_ALL + ' Save & Exit \n')
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
            save_exit()
        else:
            choice= int(input('need to choose a number between 1 and 5:'))
            continue


def view_tasks(L):
    if len(L)> 0:
        print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
        for i,e in enumerate(L,start=1):
            print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , e)
        print()
        print('[ ] = not done, [✅ ] = done')
        choice = input('press 0 to go back to Menu: ')
        if choice == 0:
            menu()
    else:
        print(Fore.GREEN,'Your To-Do List is empty, Kindly add a new task:',Style.RESET_ALL,'\n')
        menu()

def add_task():
    task= input('Enter new Task: ')
    L.append(task)
    print('Task added successfully!')
    choice = int(input('press 0 to go back to Menu or press 1 to add new task:'))
    if choice == 0:
        menu()
    elif choice == 1:
        add_task()
    

def Mark_task_asDone():
    pass

def delete_task(L):
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
        index_to_del=int(input('Kindly choose the index of the task you want to delete:'))
        if 0<=index_to_del<len(L):
            del L[index_to_del]
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
    

    

def save_exit():
    exit()


menu()
  