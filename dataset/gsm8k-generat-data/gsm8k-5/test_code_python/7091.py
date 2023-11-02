def solution():
    bikes_sold = 19 + 27  # Calculate the total number of bikes sold in a day
    bike_clamps_per_bike = 2  # Customers receive 2 bike clamps for each bike purchased

    # Calculate the total number of bike clamps given to customers
    total_bike_clamps = bikes_sold * bike_clamps_per_bike
    result = total_bike_clamps
    return result

print(solution())