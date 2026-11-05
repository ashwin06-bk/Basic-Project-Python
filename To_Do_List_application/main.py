print("\n To-Do-List Application")

print("1)Add New Task")
print("2)Show Task")
print("3)Delete Task")
print("4)Update Task")
print("5)Exit")


def main():
    while True:
        try:
            choice = int(input("Enter Your Choice: "))

            if choice ==1:
               add_task()
            elif choice == 2:
               show_task()

            elif choice ==3:
               delete_task()

            elif choice == 4:
               update_task()

            elif choice == 5:
               print("Thank You.")
               break

            else:
               print("Enter Correct Choice.")

        except ValueError:
            print("Enter Valid Number.")
tasks = []

def add_task():
    task = input("Enter Task : ")
    tasks.append(task)
    print("task added Successfuly")

def show_task():

    if len(tasks) ==0:
        print("No task Available")
    else:
        print("\nYour Task: ")
        for index, task in enumerate(tasks,start=1):
            print(index,task)

def delete_task():
    if len(tasks) == 0:
        print("No Available Task in List.")

    else:
        show_task()
        try:
            task_number = int(input("Enter Task Number: "))
            if task_number >= 1 and task_number <=len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Task Deleted Successfuly: ",deleted_task)

            else:
                print("invalid Task Number")

        except ValueError:
            print("Enter valid Task Number.")

def update_task():
    if len(tasks) == 0:
        print("No Available Task in List.")

    else:
        show_task()
        try:
            task_number = int(input("Enter Task Number to Update: "))
            if task_number>=1 and task_number <=len(tasks):
                New_task = input("Enter New Task: ")
                tasks[task_number -1] = New_task
                print("Task Updated successfuly.")

            else:
                print("Invalid Task Number.")

        except ValueError:
            print("Enter Valid Task Number.")

# add_task()
# show_task()
# delete_task()
# update_task()
main()