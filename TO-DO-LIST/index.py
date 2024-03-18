tasks = []       # Where tthe tasks will be stored

def add_task(task):      # Function to add task
    tasks.append(task)
    print("Task added successfully.")

def remove_task(task_index):   # function to remove task
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            del tasks[task_index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid task index.")

def display_tasks():      # function to display task 
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("There is no tasks in the list.")

def update_task(task_index, new_task):   # Function to update task 
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid task index.")

def main():      # defining the main function
    while True:
        print("\n         To-Do List App          ")
        print("1. To Add Task")
        print("2. To Remove Task")
        print("3. To Display Tasks")
        print("4. To Update Task")
        print("5. To Exit")

        choice = input("Enter your choice: ")

        if choice == '1':                     # That function will be called what the user want
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            task_index = input("Enter task index to remove: ")
            remove_task(task_index)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            task_index = input("Enter task index to update: ")
            new_task = input("Enter new task: ")
            update_task(task_index, new_task)
        elif choice == '5':
            print("Exited")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
