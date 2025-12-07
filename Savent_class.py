#=====================================TO-Do Aplication============================================================================

tasks = []

while True:
    print("\n------------To Do list-------------")
    print("1.Add a task")
    print("2.View task")
    print("3.Remove Task")
    print("4.Exit")

    choise = input("Enter your choise(1-4):")

    if choise == "1":
        #add a task
        task = input("enter a new task:")
        tasks.append(task) #when we want to add something on array we have to write thearrayname.append(where to store)
        print("Task added succesfull")
    elif choise == "2":
        #viwe task
        if len(tasks)==0:
            print("No task in the list")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                print(f"{i+1},{tasks[i]}")
    elif choise == "3":
        if len(tasks) ==0:
            print("No task in the list")
        else:
            print("\your task")
            for i in range (len(tasks)):
                print(f"{i+1},{tasks[i]}")

            task_no=input("Enter task number to remove:")

            #validation input is a number
            if task_no.isdigit():
                task_no = int(task_no)
                if 1<= task_no <= len(tasks):
                    remove = tasks.pop(task_no - 1)
                    print("Your task removed",remove)
                else:
                    print("Plz enter valid number:")
    elif choise == "4":
                #exit
                print("Thank you")
                break
    else:
         print("Invalid choise!")
