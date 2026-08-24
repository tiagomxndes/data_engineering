"""
Pandas Basics — Reading & Exploring Files
Theory first, then exercises. No file provided? Create tiny sample CSVs
yourself with a text editor or via code (shown below) so you can test
against real files.
"""

# ============================================================
# THEORY
# ============================================================
#
# pandas is a library for working with tabular data (rows and columns),
# similar to a spreadsheet. The core object is a DataFrame.
#
# Key commands for this section:
#
# import pandas as pd
#
# pd.read_csv(path)          -> reads a CSV file into a DataFrame
# df.head(n)                 -> shows the first n rows (default 5)
# df.tail(n)                 -> shows the last n rows
# df.info()                  -> shows column names, types, non-null counts
# df.describe()              -> summary statistics for numeric columns
# df.shape                   -> (num_rows, num_columns) tuple
# df.columns                 -> list-like of column names
# df["col_name"]             -> selects a single column (a Series)
# df[["col1", "col2"]]       -> selects multiple columns (a DataFrame)
# df[df["col"] > value]      -> filters rows based on a condition
# df["col"].mean()/.sum()/.max()/.min() -> aggregate a column
# df.sort_values("col")      -> sorts rows by a column
# df.to_csv(path, index=False) -> writes a DataFrame back to a CSV

import pandas as pd

# Run this once to create a sample file to work with:
sample_data = """name,department,salary,years_experience
Alice,Engineering,75000,3
Bob,Sales,60000,5
Charlie,Engineering,90000,7
Dave,Marketing,55000,2
Eve,Sales,65000,4
Frank,Engineering,80000,1
"""
with open("employees.csv", "w") as f:
    f.write(sample_data)


# ============================================================
# PART 1 — Isolated exercises (one concept each)
# ============================================================


# 1. Read "employees.csv" into a DataFrame and print its first 3 rows.
def show_first_rows():
    df = pd.read_csv("employees.csv")
    print(df.head(3))


show_first_rows()


print(40 * "-")


# 2. Read "employees.csv" and print df.info() and df.describe().
def show_summary():
    df = pd.read_csv("employees.csv")
    print(df.info())
    print(40 * "-")
    print(df.describe())


show_summary()


print(40 * "-")


# 3. Read "employees.csv" and print only the "name" and "salary" columns.
def show_two_columns():
    df = pd.read_csv("employees.csv")
    print(df[["name", "salary"]])


show_two_columns()

print(40 * "-")


# 4. Read "employees.csv" and print only the rows where salary > 65000.
def high_earners():
    df = pd.read_csv("employees.csv")
    print(df[df["salary"] > 65000])


high_earners()


# 5. Read "employees.csv", print the average salary, and the highest
#    years_experience value.
def print_stats():
    df = pd.read_csv("employees.csv")
    print(f"Avg salary: {df['salary'].mean()}")
    print(f"Highest years of exeperience: {df['years_experience'].max()}")


print_stats()
print(40 * "-")

# ============================================================
# PART 2 — Build from scratch (easiest → hardest)
# ============================================================

# A. EASIEST
# Write department_average(path) that reads a CSV like employees.csv and
# returns the average salary specifically for the "Engineering"
# department (not all departments).


def department_average(path):
    df = pd.read_csv(path)
    engineering_department = df[df["department"] == "Engineering"]
    return engineering_department["salary"].mean()


print(department_average("employees.csv"))
# Test with department_average("employees.csv")
# Expected output: 81666.66666666667


# B. MEDIUM
# Write top_n_earners(path, n) that reads a CSV and returns a DataFrame
# containing the top n rows sorted by salary, descending.


def top_n_earners(path, n):
    df = pd.read_csv(path)
    sorted_salary = df.sort_values("salary", ascending=False)
    return sorted_salary.head(n)


print(top_n_earners("employees.csv", 3))
# Test with top_n_earners("employees.csv", 3)
# Expected output (3 rows, sorted descending by salary):
#      name   department  salary  years_experience
# 2  Charlie  Engineering   90000                 7
# 5    Frank  Engineering   80000                 1
# 0    Alice  Engineering   75000                 3

# C. HARDEST — data engineering flavored
# Write department_summary(path) that reads a CSV and returns a dictionary where:
#   -> each key is a department name
#   -> each value isanother dictionary with "avg_salary" and "headcount" for that department.
print(40 * "-")


def department_summary(path):
    dpt_dict = {}
    df = pd.read_csv(path)
    departments = df["department"]
    for department in departments:
        if department not in dpt_dict:
            matching_rows = df[df["department"] == department]
            dpt_dict[department] = {
                "avg_salary": round(float(matching_rows["salary"].mean()), 2),
                "headcount": len(matching_rows),
            }
    return dpt_dict


print(40 * "-")


def department_summary_groupby(path):
    df = pd.read_csv(path)
    result = df.groupby("department")["salary"].agg(["mean", "count"])
    return result


print(department_summary("employees.csv"))
print(department_summary_groupby("employees.csv"))

# Test with department_summary("employees.csv")
# Expected output (values may print in a different key order):
# {
#  "Engineering": {"avg_salary": 81666.67, "headcount": 3},
#     "Sales": {"avg_salary": 62500.0, "headcount": 2},
#     "Marketing": {"avg_salary": 55000.0, "headcount": 1},
# }
