# DataFrames
## Aggregating DataFrames
### Counting 

# vet_visits is the df
# dropping duplicate names
vet_visits.drop_duplicates(subset="name")

# dropping duplicate pairs 
unique_dogs = vet_visits.drop_duplicates(subset=["name", "breed"])
print(unique_dogs)

# count dogs of each breed, by subsetting "breed" and using .value_counts method
unique_dogs["breed"].value_counts(sort=True)

# proportions obtained by using normalize argument 
unique_dogs["breed"].values_counts(normalize=True)


# Dropping duplicates
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

