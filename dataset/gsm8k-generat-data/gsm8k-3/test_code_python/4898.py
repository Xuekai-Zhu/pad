def solution():
    """There are 4 trains waiting at a train station and each train has 4 carriages. Each carriage has 3 rows of wheels and the rows of wheels have 5 wheels each. How many wheels are at the train station?"""
    # Define the number of trains and carriages
    num_trains = 4
    num_carriages_per_train = 4

    # Define the number of rows and wheels per carriage
    num_rows_per_carriage = 3
    num_wheels_per_row = 5

    # Calculate the total number of wheels
    total_wheels = num_trains * num_carriages_per_train * num_rows_per_carriage * num_wheels_per_row

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())