#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(argv[1])).json()

    with open('{}.json'.format(argv[1]), 'w') as file:
        task_list = []
        for task in tasks:
            edited_task = {"task": task['title'],
                           "completed": task['completed'],
                           "username": user['username']}
            task_list.append(edited_task)
        write_dict = {user['id']: task_list}
        file.write(json.dumps(write_dict))
