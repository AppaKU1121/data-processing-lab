# OOP Data Processing Lab

## Lab Overview
This lab is about changing procedural Python code into OOP style. It reads city data from `Cities.csv` and uses classes to filter and calculate values like average and max temperature.

## Project Structure
```
data-processing-lab/
├── README.md
├── Cities.csv
└── data_processing.py
```

## Design Overview
1. `DataLoader`
- Used to load data from a CSV file.
- Attributes: `base_path` (folder path of the file)
- Methods: `load_csv(filename)` reads the CSV file and returns a list of dictionaries.

2. `Table`
- Used to store table data and do operations on it.
- Attributes: `table_name` (name of the table), `table` (list of dictionaries)
- Methods:
  - `filter(condition)` returns a new `Table` with rows that match the condition.
  - `aggregate(aggregation_function, aggregation_key)` calculates a summary value (like average or max) from a specific column.

## How to Test and Run Your Code
1. Put `data_processing.py` and `Cities.csv` in the same folder.
2. Open terminal and run:
```
python data_processing.py
```