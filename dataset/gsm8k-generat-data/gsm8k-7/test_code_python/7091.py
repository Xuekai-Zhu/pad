def solution():
    bikes_sold_morning = 19
    bikes_sold_afternoon = 27
    bike_clamps_per_bike = 2

    # Calculate the total number of bikes sold
    total_bikes_sold = bikes_sold_morning + bikes_sold_afternoon

    # Calculate the total number of bike clamps given to customers
    total_clamps_given = total_bikes_sold * bike_clamps_per_bike
    result = total_clamps_given
    return result

print(solution())