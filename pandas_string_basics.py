# import pandas and use an alias to shorten the code

import pandas as pd
import string

# Creating a dataframe

sales = {"user_id": ["KM37", "PR19", "YU88"], "order_value": [197.75, 208.21, 134.99]}

sales_df = pd.DataFrame(sales)

print(sales_df)

# Reading a CSV file in our current directory

csv_file = pd.read_csv("customers-100.csv")
print(csv_file)

# Help on package with pandas
# print(help(pd))

# ascii_lowercase attribute return all lower case letters

print(string.ascii_lowercase)

# digits attribute returns all digits from 0-9
print(string.digits)

# ponctuation returns all the special characters

print(string.punctuation)
