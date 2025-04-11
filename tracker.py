import argparse
import random
import csv
from collections import defaultdict
from datetime import date
import os
from collections import Counter

def main():
    '''
    The main logic of the module.
    Creates the valid arguments needed to be handled
    Takes in a task and person and logs it to a CSV with the day and time it was completed
    '''

    DAILY_TASKS = ['vacuum', 'laundry', 'reading', 'writing', 'cleaning']

    # Having all of the CLI parsing and subparsing in one grouping for clarity
    parser = argparse.ArgumentParser(description = "Daily Task Tracker")
    subparsers = parser.add_subparsers(dest = "command", required = True)

    add_parser = subparsers.add_parser("add", help = "Add a person and their task.")
    add_parser.add_argument("--task", required = True, type=str, help = "The tasking being performed.")
    add_parser.add_argument("--person", required = True, type = str, help = "Who performed the task.")
    add_parser.add_argument("--verbose", action = "store_true", help = "Enable verbose logging.")

    stats_parser = subparsers.add_parser("stats", help = "Check the stats of a particular person and task.")
    stats_parser.add_argument("--task", type = str, help = "pulls the frequency of the persons task.")
    stats_parser.add_argument("--person", type = str, help = "pulls the stats of the given person.")
    stats_parser.add_argument("--last", type = int, help = "checks the last x amount of task instances.")

    args = parser.parse_args()

    if args.command == "add":
        task = cleaned_text(args.task)
        person = cleaned_text(args.person)
        verbose = args.verbose

        # Putting palindromic in verbose to avoid too much CLI output unless wanted.
        if verbose:
            print(f"Logging task: '{task}' by {person}")
            palindromic = cleaned_text(task)
            if palindromic == palindromic[::-1]:
                print(f"Fun fact, {task} is a palindrome!")    
        print(f"Task - {task} - received! Now logging..")

        # Grouping the csv logic lines for cleaner code spacing.
        add_task_and_person(task, person, verbose)

    if args.command == "stats":
        task = cleaned_text(args.task) if args.task else None
        person = cleaned_text(args.person) if args.person else None
        number = args.last
        print(pull_stats(task, person, number))


def cleaned_text(s):
    '''
    Removes any unecessary capitalization and special characters for uniform data
    Args:
        s [str]
    Returns:
        string that is lowercased and only alphanumeric
    '''
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned


def add_task_and_person(task, person, verbose):
    '''
    Takes a task, a person, and the verbose optionality
    adds task and person to the tasks.csv
    Args:
        task [str]
        person [str]
    '''
    today = date.today().isoformat()
    row = [task, person, today]

    file_exists = os.path.isfile("tasks.csv")

    with open("tasks.csv", mode = "a", newline = '') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Task", "Person", "Date"])
        writer.writerow(row)

        if verbose:
            print(f"Completed: logged task to csv -> {row}")
        else:
            print("Completed Logging.")



def pull_stats(task, person, number):
    '''
    Checks the stats of a particular person, task, and/or how often they did it in their last {number} times
    Args:
        task -> [str] to check the amount of times they did a task
        person -> [str] for stat checking
        number -> [int] to collect the last number of entries
    '''
    stats_dict = defaultdict(int)
    with open("tasks.csv", 'r', newline = '') as f:
        reader = csv.reader(f)
        next(reader)

        rows = list(reader)
        if number:
            rows = rows[-number:]
        for row in rows:
            if row[1] == person:
                stats_dict[row[0]] += 1

    output = f"\nTask stats for {person}:\n"
    for task, count in sorted(stats_dict.items(), key = lambda x: x[1], reverse = True):
        output += f'- {task} : {count}\n'

    return output


if __name__ == "__main__":
    main()