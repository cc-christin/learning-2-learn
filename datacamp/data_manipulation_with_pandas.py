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

