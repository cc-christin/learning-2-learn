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

