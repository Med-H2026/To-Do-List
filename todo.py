import json
from colorama import Fore,Back,Style,init # use colorama library for text coloration
L=[] # define a list where to add my task
saved = True # track if any changes already saved or not

# display all aspects of our Todo list app 
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
            choice= int(input('need to choose a number between 1 and 6:'))
            continue

# display all tasks already saved in our json file
def view_tasks(L : list)->None:
    with open('To-Do-List.json','r',encoding='utf-8') as f:  # open a json file on reading mode
        L = json.load(f)                                     # load data from file
    if len(L)> 0:
        print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
        for i,task in enumerate(L, start=1):
            if task['done']:                                                         # check if task is already marked as done
                print('[✅ ]',Fore.RED , i,'.' , Style.RESET_ALL , task['name'])    # if already marked as done, print with checked tag
            else:
                print('[ ]',Fore.RED , i,'.' , Style.RESET_ALL , task['name'])       # if not marked as done, print without checked tag
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
# add new task 
def add_task() -> None:
    global saved 
    with open('To-Do-List.json','r',encoding='utf-8') as f: # open file on read mode
        L = json.load(f)                                    # load data from file
    task= input('Enter new Task: ')                         # enter new task
    L.append({'name':task, 'done':False})                   # add task to list as a dictionary data
    saved = False                                           # notification of a new changes
    save_to_file(L)                                         # save to json file
    print(Fore.GREEN,'Task added successfully!',Style.RESET_ALL)
    choice = int(input('press 0 to go back to Menu or press 1 to add new task:'))
    if choice == 0:
        menu()
    elif choice == 1:
        add_task()
    
# edit existing task
def edit_task(L : list) -> None:
    
    while True:
        global saved
        index_task = int(input('Kindly type the task number which you want to edit:')) # choose the task number to be edited
        new_msg = input('Please type your new Task:')                                  # enter the new task 
        if 0<index_task<=len(L):                                                       # check if the number selected is within the range 
            L[index_task-1] = {'name':new_msg, 'done':L[index_task-1]['done']}         # add to list
            saved = False                                                              # notification of new changes
            save_to_file(L)                                                            # save edited task to file
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

# mark existing task as done
def Mark_task_asDone(L : list) -> None:
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
        choice = int(input('Please enter the number of the task you want to mark as done or press 0 to go back to menu: ')) # select the task u want to mark as done
        if 0<choice<= len(L):                                                                                               # check if selected number is within the range
            if task['done'] == False:                                                                                       # check if the task not marked as done
                L[choice-1] = {'name':L[choice-1]['name'],'done':True}                                                      # edit the list with new updates
                saved = False                                                                                               # notification for new changes
                save_to_file(L)                                                                                             # save to file
                print(Fore.GREEN,'Your Tasks:',Style.RESET_ALL)
                for i,task in enumerate(L,start=1):
                    if task['done']:
                        print('[✅ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                    else:
                        print('[ ]',Fore.RED,i,'.',Style.RESET_ALL,task['name'])
                print()
                print('[ ] = not done, [✅ ] = done')
            else:                                                                                                          # check if already marked and want to unmark(means not yet done)
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

# delete existing task by selecting its number from ToDo list tasks
def delete_task(L : list) -> None:
    global saved
    with open('To-Do-List.json','r',encoding='utf-8') as f:
        L = json.load(f)
    if len(L)> 0:                                                           # check if list not empty so we print all existing tasks
        print(Fore.GREEN + 'Your Tasks: ' + Style.RESET_ALL)
        for i,task in enumerate(L,start=1):
            if task['done']:
                print('[✅ ]', Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
            else:
                print('[ ]', Fore.RED , i,'.' , Style.RESET_ALL , task['name'])
        print()
        print('[ ] = not done, [✅ ] = done')
    else:                                                                   # if list empty, display a warning msg
        print(Fore.GREEN,'Your To-Do List is empty, Kindly add a new task:',Style.RESET_ALL,'\n')
        menu()
    while True:                                                             
        index_to_del=int(input('Kindly choose the index of the task you want to delete or press 0 to go back to menu:')) # select the task number to delete
        if index_to_del == 0:                                                                                            # if selected number is 0, redirect to the main menu
            menu()
        elif 0<index_to_del<=len(L):                                        # check if selected number is within the range, so we can delete 
            del L[index_to_del-1]                                           # delete the task
            saved = False                                                   #notification of new changes
            save_to_file(L)                                                 # save changes to file
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
# save changes to a json file, to be loaded later when needed    
def save_to_file(L : list) -> None:
    global saved
    if not saved:                                                              # use the global variable 'saved' to check if any new changes happened
        with open('To-Do-List.json','w',encoding='utf-8') as f:                # open a json file on write mode
            json.dump(L,f, indent=4)                                           # write into file using dump method
        saved = True                                                           # notify app that all changes are saved
    else:
        print('\n',Fore.GREEN,'File already Saved!',Style.RESET_ALL,'\n')

# exit the app after checking if all changes are saved and file updated   
def exit_app(L : list) -> None:
    if not saved:                                                             # check if any changes before exiting
        msg = input('you have unsaved changes, save before exiting? y/n: ')   
        if msg.lower() == 'y':                                                # if yes do save changes and update file
            save_to_file(L)
    print('Goodbye!')
    exit()                                                                    # exit app

# main method to run our app
def main() -> None:
    menu()                                                                    # call menu method to display all app aspects

if __name__ == '__main__':                                                     # only run the main method if this file was run directly
    main()
  