## The Goal of This Project
- to reinforce some built-in python packages and concepts

### Daily Task Tracker Using a CLI
1. Take user input from the command line (argparse)
2. Read and write to a CSV file (csv.reader, csv.writer)
3. Add new tasks with metadata (task, person, timestamp)
4. Count how often each task is done (Counter)
5. Randomly shuffle tasks for assignment (random.shuffle)
6. Validate input - check if task name is a palindrome just for fun (isalnum, [::-1])
7. Check if all required fields are filled (all())
8. Handle missing task types or people with defaults (dict.get())
9. Sort tasks by frequency (sorted, lambda)
10. Timestamp tasks with today's date (datetime)

#### Example Usage
```bash
python tracker.py --task "email cleanup" --person "Alice"
```

Then:
- appends the task to tasks.csv
- validates it
- shows how often that task has been logged
- optionally shows all task frequencies in descending order
