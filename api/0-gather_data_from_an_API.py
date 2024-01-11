#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

if __name__ == '__main__':
    import requests
    from sys import argv

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(argv[1]))
    completed_list = []
    completed_tasks = 0
    total_tasks = 0

    employee_name = user.json()['name']
    for task in tasks.json():
        total_tasks += 1
        if task['completed'] is True:
            completed_list.append(task['title'])
            completed_tasks += 1

    print("Employee {} has completed tasks({}/{}):".
          format(employee_name, completed_tasks, total_tasks))
    for task in completed_list:
        print("\t {}".format(task))