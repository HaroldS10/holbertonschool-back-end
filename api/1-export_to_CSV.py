#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            row = [user['id'], user['username'],
                   task['completed'], task['title']]
            writer.writerow(row)
