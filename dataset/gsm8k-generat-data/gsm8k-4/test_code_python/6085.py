def solution():
    """Carol spends five hours filling up her pool. During the first hour, the pool fills at a rate of 8 gallons of water per hour. For the next two hours, the pool fills at 10 gallons of water per hour. For the fourth hour, the pool fills at a rate of 14 gallons of water per hour. During the fifth hour, the pool develops a leak and loses 8 gallons of water. At the end of five hours, how many gallons of water are still left in the pool?"""
    # Define the total time taken to fill the pool
    total_time = 5

    # Define the rate of water flow for each hour
    rate = [8, 10, 10, 14, 0]

    # Initialize the total amount of water in the pool
    water_in_pool = 0

    # Calculate the amount of water added to the pool during each hour
    for i in range(total_time):
        water_in_pool += rate[i]

    # Subtract the water loss due to the leak in the fifth hour
    water_in_pool -= 8

    # Display the amount of water left in the pool at the end of five hours
    result = water_in_pool
    return result

print(solution())