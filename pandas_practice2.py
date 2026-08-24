import pandas as pd


# Read File and create Data Frame
df = pd.read_csv("employees.csv")

print("DataFrame:")
print(df)
print(40 * "-")

print("First n rows: ")
print(df.head(3))
print(40 * "-")

print("DadaFrame info:")
print(df.info())
print(40 * "-")

print(df["department"])
print(40 * "-")

print("DataFrame tail: ")
print(df.tail(2))
print(40 * "-")

print("DataFrame describe:")
print(df.describe())
print(40 * "-")

print("DataFrame shape:")
print(df.shape)  # Returns number of rows and columns
print(40 * "-")

print("DataFrame columns:")
print(df.columns)  # list with the names of the columns

for column in df.columns:
    print(column)

print("Years of experience column: (single column)")
print(df["years_experience"])
print(40 * "-")

print("Years of experience and department columns: ")
print(df[["years_experience", "department"]])
print(40 * "-")

print("Print salaries bigger than 75'000")
print(df[df["salary"] > 75000])
print(40 * "-")

print("Sort values by column name: ")
print(df.sort_values("salary", ascending=False))
