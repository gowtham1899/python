def manage_data():
    # List
    tasks = ["email", "meeting", "code review"]
    tasks.append("lunch break")
    
    # Dictionary
    employee = {"name": "Emma", "role": "Developer", "tasks": tasks}
    
    # Set
    completed_tasks = {"email", "meeting"}
    
    # Tuple
    work_hours = (9, 17)

    print("Employee:", employee["name"])
    print("Work Hours:", work_hours)
    
    print("\nTask Status:")
    for task in employee["tasks"]:
        status = "Done" if task in completed_tasks else "Pending"
        print(f"- {task}: {status}")

manage_data()
