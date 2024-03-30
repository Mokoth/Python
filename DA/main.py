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

# # Task
# Convert the AppleStore.csv file into a list of lists and assign that list to a variable named apps_data.

# Create an empty list named ratings.
# Iterate over apps_data[1:] (which excludes the header row), and for each iteration (row), 
# we do the following:
# Extract the rating and convert it to a float using float(row[7]). 
# The rating has the index number 7 and comes as a string, so we need to convert it to a float.
# We assign the rating to a variable named rating.
# We append rating to the ratings list we created outside the loop using ratings.append(rating) function.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    ratings.append(rating)
print(ratings[:5])

# Task

# Inside the for loop, complete the following:
# Get the name of the app and store it in a variable called name. 
# The name is the second item in each row.
# Append the value stored in name to the apps_names list using the list_name.append() function
#  (note the apps_names list is already defined in the code editor) and be careful with indentation.
# Print the first 5 elements in apps_names list to display the names of the apps.

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    name = row[1]
    apps_names.append(name)
print(apps_names[:5])


# In the diagram below, we created a list of lists named app_and_price, and we want to extract the names of the free apps in a separate list. To do that, complete the following:

# Create an empty list named free_apps.
# Iterate over app_and_price. For each iteration, we do the following:
# Extract the name of the app and assign it to a variable named name.
# Extract the price of the app and assign it to a variable named price.
# Append the name of the app to free_apps (the empty list that we initialized outside the loop) if the price of the app equals 0.

app_and_price = [['Facebook', 0], ['Instagram', 0], ['Tiktok', 2.99], ['Temple Run', 4.55], ['Zombies', 0]]

free_apps = []
for row in app_and_price:
    name = row[0]
    price = row[1]

    if price == 0:
        free_apps.append(name)

print(free_apps)

# Task

# Using the same techniques in the diagram above, compute the average rating of non-gaming apps.

# Initialize an empty list named non_games_ratings.
# Loop through the apps_data list of lists (make sure you don't include the header row). For each iteration of the loop, do the following:
# Assign the rating of the app as a float to a variable named rating (the index number of the rating column is 7).
# Assign the genre of the app to a variable named genre (index number 11).
# If the genre is not equal to 'Games', append the rating to the non_games_ratings list.
# Compute the average rating of non-gaming apps and assign the result to a variable named avg_rating_non_games.

# Optional exercise: compare the average rating of gaming apps (3.69) with the average rating of non-gaming apps. Why do you think we see this difference?

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # print(type(rating))
    genre = row[11]
    if genre != 'Games':
        non_games_ratings.append(rating)
# print(avg)
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)
print(avg_rating_non_games)


# 
catNames = []

while True:
    print(f'Enter cat name {len(catNames) + 1} (Enter nothing to exit.)')
    name = input()
    if name == '':
        break
    catNames.append(name)
print('Cat names are:')
for row in catNames:
    print('' + row)