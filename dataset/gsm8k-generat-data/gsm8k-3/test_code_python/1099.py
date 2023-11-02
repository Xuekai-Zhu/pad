def solution():
    """A hot dog stand sells 10 hot dogs every hour, each one selling for $2.  How many hours does the stand need to run to make $200 in sales?"""
    # Define the price of each hot dog and the target sales amount
    HOT_DOG_PRICE = 2
    TARGET_SALES = 200

    # Calculate the number of hot dogs needed to reach the target sales amount
    hot_dogs_needed = TARGET_SALES / HOT_DOG_PRICE

    # Calculate the number of hours needed to sell that many hot dogs
    hours_needed = hot_dogs_needed / 10

    # Display the number of hours needed
    result = hours_needed
    return result

print(solution())