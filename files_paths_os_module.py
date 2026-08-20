# ============================================================
# WEEK 7 — FILES, PATHS & THE os MODULE
# Backend / Data Engineering Focus
# ============================================================

# Goal:
# Learn to work with the filesystem.
#
# By the end of this week you should be comfortable:
#
# - Finding your current directory
# - Listing files
# - Building file paths correctly
# - Checking if files/folders exist
# - Distinguishing files from directories
# - Writing small utilities that resemble real backend/ETL scripts
#
# IMPORTANT:
#
# Don't look anything up.
#
# If you get stuck:
#
# 1. Write what you tried.
# 2. Explain where you got stuck.
# 3. Then ask for help.
#
# ============================================================
# PART 1 — THEORY + ISOLATED EXERCISES
# ============================================================


# ------------------------------------------------------------
# THEORY: Current Working Directory
# ------------------------------------------------------------
#
# Every Python program runs from a CURRENT WORKING DIRECTORY.
#
# Think of it as:
#
#     "Where is my program currently standing?"
#
# Example:
#
#     /home/tiago/projects/backend
#
# If your code does:
#
#     open("users.csv")
#
# Python will actually look for:
#
#     /home/tiago/projects/backend/users.csv
#
# To see the current working directory:
#
#     import os
#
#     os.getcwd()
#
# It returns a STRING.
#
# This is one of the first things backend developers print
# when debugging file problems.


# 1.
# Write a function:
#
#     show_current_directory()
#
# that prints the current working directory.

import os
from os.path import isdir


def show_current_directory():
    print(os.getcwd())


show_current_directory()

print(40 * "-")


# ------------------------------------------------------------
# THEORY: Listing Files
# ------------------------------------------------------------
#
# Often you need to inspect a folder.
#
# Python provides:
#
#     os.listdir(path)
#
# Example:
#
#     os.listdir(".")
#
# "." means:
#
#     the current directory
#
# It returns a LIST of names.
#
# Example:
#
# [
#     "main.py",
#     "users.csv",
#     "logs"
# ]
#
# Notice:
#
# It does NOT tell you whether something is a file
# or a directory.
#
# Only the names.


# 2.
# Write a function:
#
#     list_current_directory()
#
# that prints every item inside the current directory.


def list_current_directory():
    cwd = os.getcwd()

    print(os.listdir(cwd))


list_current_directory()

print(40 * "-")


# ------------------------------------------------------------
# THEORY: Building Paths
# ------------------------------------------------------------
#
# Never manually build file paths.
#
# BAD:
#
#     folder + "/" + filename
#
# because Windows uses "\" while Linux/macOS use "/".
#
# Instead use:
#
#     os.path.join()
#
# Example:
#
# folder = "logs"
# filename = "today.log"
#
# path = os.path.join(folder, filename)
#
# Linux:
#
# logs/today.log
#
# Windows:
#
# logs\today.log
#
# Python automatically chooses the correct separator.


# 3.
# Write a function:
#
#     build_log_path(filename)
#
# that returns the path:
#
# logs/<filename>
#
# using os.path.join()


def build_log_path(filename):
    path = os.path.join("logs", filename)

    return path


print(build_log_path("today.log"))

print(40 * "-")


# ------------------------------------------------------------
# THEORY: Does Something Exist?
# ------------------------------------------------------------
#
# Before opening a file, backend code often checks whether
# it actually exists.
#
# Use:
#
#     os.path.exists(path)
#
# It returns:
#
# True
#
# or
#
# False


# 4.
# Write a function:
#
#     file_exists(path)
#
# Return True if the path exists.
#
# Otherwise return False.


def file_exists(path):
    return os.path.exists(path)


print(file_exists("test.txt"))

print(40 * "-")


# ------------------------------------------------------------
# THEORY: File or Directory?
# ------------------------------------------------------------
#
# Sometimes you need to know whether a path is:
#
# - a file
# - a directory
#
# Python provides:
#
# os.path.isfile(path)
#
# and
#
# os.path.isdir(path)
#
# These return True or False.


# 5.
# Write a function:
#
#     describe_path(path)
#
# Return:
#
#     "file"
#
# if it's a file.
#
# Return:
#
#     "directory"
#
# if it's a directory.
#
# Otherwise return:
#
#     "missing"


def describe_path(path):
    if os.path.isdir(path):
        return "directory"

    if os.path.isfile(path):
        return "file"

    return "missing"


print(describe_path("."))

print(40 * "-")


# ============================================================
# PART 2 — EASY COMBINED EXERCISES
# ============================================================

#
# These combine several concepts.
#
# Don't overthink them.
#
# Think:
#
# - What data do I have?
# - Which os function do I need?
# - Do I need a list?
# - Do I need a counter?
#


# ------------------------------------------------------------
# A. Find Python files
# ------------------------------------------------------------
#
# Write:
#
#     find_python_files(path)
#
# Return a LIST containing every filename ending with:
#
#     .py
#
# Hint:
#
# You'll combine:
#
# - os.listdir()
# - a loop
# - string methods


def find_python_files(path):
    list_filenames = []

    files = os.listdir(path)

    for file in files:
        if file.endswith(".py"):
            list_filenames.append(file)

    return list_filenames


print(find_python_files("."))


# ------------------------------------------------------------
# B. Count Files
# ------------------------------------------------------------
#
# Write:
#
#     count_files(path)
#
# Return how many FILES exist inside the directory.
#
# Ignore directories.
#
# Hint:
#
# os.listdir()
#
# +
#
# os.path.isfile()


"""
First version test:

directory_content = os.listdir(path)

for content in directory_content:
    if os.path.isfile(content):

the problem here is that content is ONLY THE FILENAME not the LOCATION OF THE FILE.

os.listdir() -> Gives you the name.
os.path.join() -> gives the location.
"""


def count_files(path):
    counter = 0
    directory_content = os.listdir(path)

    for content in directory_content:
        full_path = os.path.join(path, content)

        if os.path.isfile(full_path):
            counter += 1

    return counter


print(count_files("."))


# ------------------------------------------------------------
# C. Build Project Paths
# ------------------------------------------------------------
#
# Write:
#
#     build_project_paths(project_name)
#
# Return a tuple containing:
#
# (
#     project_folder,
#     config_path,
#     logs_path
# )
#
# Use os.path.join().


"""
My mistake:

I interpreted the exercise as like a folder inside a folder when in reality,
it's the project folder and inside we have the two different ones:
    -> config_path
    -> logs_path

bruh..

def build_project_paths(project_name):
    project_folder = project_name
    config_path = os.path.join(project_folder, "config"_)
    logs_path = os.path.join(config_path, "logs")

    return project_folder, config_path, logs_path
"""


def build_project_paths(project_name):
    project_folder = project_name
    config_path = os.path.join(project_folder, "config")
    logs_path = os.path.join(project_folder, "logs")

    return project_folder, config_path, logs_path


print(build_project_paths("my_project"))
# -> ('my_project', 'my_project/config', 'my_project/logs')


print(40 * "-")


# ============================================================
# PART 3 — BUILD FROM SCRATCH
# ============================================================

#
# These resemble the kind of helper scripts you might build
# for backend services or ETL pipelines.
#
# Think before coding.
#
# Which variables should be:
#
# - list?
# - set?
# - integer?
# - tuple?
#


# ------------------------------------------------------------
# A. EASIEST — Find log files
# ------------------------------------------------------------
#
# Write:
#
#     find_log_files(path)
#
# Return a LIST containing every filename ending with:
#
#     .log


def find_log_files(path):
    folder_content = os.listdir(path)
    ending_with_log = []

    for content in folder_content:
        if content.endswith(".log"):
            ending_with_log.append(content)

    return ending_with_log


print(find_log_files("test_logs"))
print(40 * "-")

# ------------------------------------------------------------
# B. EASY / MEDIUM — Organize uploads
# ------------------------------------------------------------
#
# Given:
#
# [
#     "cat.jpg",
#     "resume.pdf",
#     "dog.png",
#     "notes.txt",
# ]
#
# Return:
#
# {
#     "jpg": ["cat.jpg"],
#     "pdf": ["resume.pdf"],
#     "png": ["dog.png"],
#     "txt": ["notes.txt"],
# }
#
# Hint:
#
# Think about dictionaries.


def organize_uploads(files):
    org_dict = {}

    for file in files:
        _, extension = os.path.splitext(file)

        if extension not in org_dict:
            org_dict[extension] = []
        org_dict[extension].append(file)

    return org_dict


print(
    organize_uploads(
        [
            "cat.jpg",
            "resume.pdf",
            "dog.png",
            "notes.txt",
            "hello.jpg",
        ]
    )
)

print(40 * "-")
# ------------------------------------------------------------
# C. MEDIUM — Scan Project
# ------------------------------------------------------------
#
# Write:
#
#     scan_project(path)
#
# Return a tuple containing:
#
# 1. Number of files
# 2. Number of directories
# 3. A SET containing every unique file extension
#
# Example:
#
# (
#     12,
#     4,
#     {"py", "csv", "json"}
# )


def scan_project(path):
    content_folder = os.listdir(path)
    num_files = 0
    num_dir = 0
    unique_ext = set()

    for content in content_folder:
        full_path = os.path.join(path, content)

        if os.path.isdir(full_path):
            num_dir += 1
        elif os.path.isfile(full_path):
            num_files += 1

            _, extension = os.path.splitext(content)
            if extension:
                unique_ext.add(extension[1:])

    return num_files, num_dir, unique_ext


print(scan_project("sample_project"))


# ------------------------------------------------------------
# D. HARD — Log Summary
# ------------------------------------------------------------
#
# Given a directory,
# return a tuple containing:
#
# 1. Total .log files
# 2. Total .txt files
# 3. Set of unique extensions
# 4. List of filenames longer than 20 characters
#
# Think carefully about which variables should be
# integers, lists and sets.


def log_summary(path):
    pass


# ------------------------------------------------------------
# E. HARDEST — Mini Dataset Scanner
# ------------------------------------------------------------
#
# Data engineering flavored.
#
# Imagine someone gives you a folder full of data.
#
# Write:
#
#     scan_dataset(path)
#
# Return a tuple containing:
#
# 1. List of CSV files
# 2. List of JSON files
# 3. Set of every unique extension found
# 4. Total number of files
# 5. Total number of directories
#
# This is similar to a utility that runs before an ETL
# pipeline begins processing data.


def scan_dataset(path):
    pass
