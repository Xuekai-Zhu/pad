def solution():
    """There are 4 trains waiting at a train station and each train has 4 carriages. Each carriage has 3 rows of wheels and the rows of wheels have 5 wheels each. How many wheels are at the train station?"""
    # Define the number of trains, carriages, rows, and wheels per row
    NUM_TRAINS = 4
    NUM_CARRIAGES = 4
    NUM_ROWS = 3
    NUM_WHEELS_PER_ROW = 5

    # Calculate the total number of wheels at the train station
    total_wheels = NUM_TRAINS * NUM_CARRIAGES * NUM_ROWS * NUM_WHEELS_PER_ROW

    # return the result
    result = total_wheels
    return result

print(solution())