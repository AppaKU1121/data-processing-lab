# OOP Data Processing Lab

## Lab Overview
This lab is about processing data from `Cities.csv` and `Countries.csv` using OOP style in Python. It uses classes to store tables in a database, filter rows, calculate values, and join two tables together.

## Project Structure
```
data-processing-lab/
├── README.md
├── Cities.csv
├── Countries.csv
└── data_processing.py
```

## Design Overview
1. `DataLoader`
- Used to load data from CSV files.
- Attributes: `base_path` (folder path of the file)
- Methods: `load_csv(filename)` reads the CSV file and returns a list of dictionaries.

2. `DB`
- Used to store multiple tables in a database list.
- Attributes: `database` (list of `Table` objects)
- Methods:
  - `insert(table)` adds a table into the database.
  - `search(table_name)` finds and returns a table by its name.

3. `Table`
- Used to store table data and do operations on it.
- Attributes: `table_name` (name of the table), `table` (list of dictionaries)
- Methods:
  - `filter(condition)` returns a new `Table` with rows that match the condition.
  - `aggregate(aggregation_function, aggregation_key)` calculates a summary value from a specific column.
  - `join(other_table, key)` combines two tables together using a common key (`country`) and returns a new `Table`.

## How to Test and Run Your Code
1. Put `data_processing.py`, `Cities.csv`, and `Countries.csv` in the same folder.
2. Open terminal and run:
```
python data_processing.py
```