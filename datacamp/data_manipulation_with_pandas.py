# DataFrames
## Aggregating DataFrames
### Counting 

# Import dependencies 
# import pandas as pd

# vet_visits is the df
# dropping duplicate names

# vet_visits.drop_duplicates(subset="name")

# dropping duplicate pairs 
# unique_dogs = vet_visits.drop_duplicates(subset=["name", "breed"])
# print(unique_dogs)

# count dogs of each breed, by subsetting "breed" and using .value_counts method
# unique_dogs["breed"].value_counts(sort=True)

# proportions obtained by using normalize argument 
# unique_dogs["breed"].values_counts(normalize=True)

# Dropping duplicates
# Import dependencies 
# import pandas as pd 

# sales is the df
# Drop duplicates store/type combinations 
# drop_duplicates()
# subset "store", "type"
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]==True].drop_duplicates("date")

# Print date column of holiday_dates
print(holiday_dates["date"])

# Counting categorical variables 

# Count the number of stores of each type
# df -> store_types
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
# normalize argument
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
# df -> store_depts
# sort argument
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalizze=True)
print(dept_props_sorted)

# Grouped Summary Statistics 
# df -> dogs

# dogs[dog["color"] == "Black"]["weight_kg"].mean()

# .groupby
# dogs.groupby("color")["weight_kg"].mean() 

# multiple grouped summaries
# .agg
# dogs.groupby("color")["weight_kg"].agg([min, max, sum])

# grouping by multiple variables
# df -> dogs
# columns -> "color", "breed"
# dogs.groupby(["color", "breed"])["weight_kg"].mean()

# goupby multiple columns and aggragate by multiple columns 
# dogs.goupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()

# What percentage of sales occurred at each store type?
# df -> sales
# import dependencies
import pandas as pd

# calculate total weekly sales
sales_all = sales["weekly_sales"].sum()

# subset for type A stores, calculate total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

#subset for type B stores, calculate total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# subset for type C stores, calculate total weekly sales
sales_c = sales[sales["type"] == "C"]["weekly_sales"].sum()

# get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / (sales_A + sales_B, sales_C)
print(sales_propn_by_type)

# Calculations with .groupby()
# df -> sales
# import pandas as pd

# Group by type; calulate total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type /sum(sales.weekly_sales)
print(sales_propn_by_type)

# group by type and is_holiday; calculate total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# Multiple grouped summaries
# Import dependencies
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)

# pivot tables
"""
dogs.pivot_table(values="weight_kg", index="color")
# takes defulted .mean() of each group

# different statistics (other than mean)
# import numpy as np 
dog.pivot_table(values="weight_kg", index="color", aggfunc=np.median)

# multiple statistics 
dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.mean, np.median])

# pivot on two variables
dog.pivot_table(values="weight_kg", index="color, columns="breed")

# filling missing values in pivot tables 
dogs.pivot_tables(values="weight_kg", index="color", colums="breed", fill_values=0)

# summing with pivot tables using margins=True
dogs.pivot_tables(values="weight_kg", index="color", colums="breed", fill_values=0, margins=True)

"""

# Pivoting on one variable
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_type(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import Dependencies
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table()

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Fill in missing values and sum values with pivot tables
# Import Dependencies
import pandas as pd

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))

# sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

# Slicing and Indexing DataFrames
# Explicity Indexes
# df -> dogs

# index object of column names
dogs.columns

# index object of row numbers
dogs.index

# setting column as index
dogs_ind = dogs.set_index("name")

# undo; reset index 
dogs_ind.reset_index()

# discard/drop index
dogs_ind.reset_index(drop=True)

# Indexes makes subsetting cleaner
# loc focuses on index values

# Subsetting Example w/out indexing
# dogs[dogs["name"].isin(["Bella", "Stella"])

# Subsetting Example when name is indexed
dogs_ind.loc[["Bella", "Stella"]]

# Index values do not have to be unique
# Subsetting on duplicate index values using loc
dogs_ind2.loc["Labrador"]
# Returns all values for applicable data

# Multiple/Hierarchical Indexes
dogs_ind3 = dogs.set_index(["breed", "color"])
print(dogs_ind3)

# Subset outer level of index with a list 
dogs_ind3.loc[["Labrador", "Chihuahua"]]

# Subset inner levels with a list of tuples
dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]]

# recap
# sorting all index values; outer to inner in ascending by .sort_index()
dogs_ind3.sort_index()

# control sort_index()
dogs_ind3.sort_index(level=["color", "breed"], ascending = [True, False])

# Setting and removing indexes
# Import Dependencies
# import Pandas as pd
# df -> temperatures

# View temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# View temperatures_ind
print(temperatures_ind)

# reset index, keeping contents
print(temperatures_ind.reset_index())

# Reset index, dropping contents
print(temperatures_ind.reset_index(drop=True))

# Subsetting with .loc[]
# import pandas as pd
# df -> temperatures
# df2 -> temperatures_ind = temperatures.set_index("city")

# list of cities to subset on 
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets aka w/out indexing
print(temperatures[temperatures["city"].isin(cities)])

# subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# indexing allows for more concise code when subsetting rows via .loc[]

# Setting multi-level/hierarchical indexes
# import pandas as pd
# df -> temperatures

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [[("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]]

# Subset for rows_to_keep
print(temperatures_ind.loc[rows_to_keep])

# Sorting by index values
# .sort_values()
# .sort_index()

# import pandas as pd
# df -> temperatures_ind
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = "city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level = ["country", "city"], ascending = [True, False]))