from csv import reader

opened_file = open('filename.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

for row in apps_data:
    first_row = row[0]
    print(first_row)


rating_sum = 0
for row in apps_data:
    last_row = row[-1]
    rating_sum = rating_sum + last_row
    # print(sum)
print(rating_sum)

# Using the new technique we've learned, calculate the average app rating for all of the 7,197 apps stored in our dataset.

# Initialize an empty list named rating_sum.
rating_sum = []
# Loop through the apps_data[1:] list of lists (don't include the header row). 
# For each of the 7,197 iterations of the loop, do the following:
apps_data = apps_data[1:]
for row in apps_data:
# Extract the rating of the app, and store it to a variable named rating 
# (the rating has the index number 7). Convert the rating value from a string to a float.
    rating = float(row[7])
# Append the value stored in rating to the list rating_sum.
    rating_sum.append(rating)
# Calculate the sum of all ratings using the sum() function.
sum_of_ratings = sum(rating_sum)
# Divide the sum of all ratings by the number of ratings, 
# and assign the result to a variable named avg_rating.
avg_rating = sum_of_ratings / len(apps_data)
# Print the results of avg_rating.
print(avg_rating)