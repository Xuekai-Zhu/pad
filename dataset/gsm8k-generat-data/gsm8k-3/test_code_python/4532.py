def solution():
    """Mr. Reyansh has a dairy farm with 40 cows. Each cow on the farm drinks 80 liters of water daily. He also has a sheep ranch with 10 times the number of cows, with each sheep drinking 1/4 times as much water as a cow does. How many liters of water does Mr. Reyansh use to water all of his animals in a week?"""
    # Define the number of cows and the amount of water each cow drinks daily
    num_cows = 40
    cow_daily_water = 80

    # Define the number of sheep and the amount of water each sheep drinks daily
    num_sheep = 10 * num_cows
    sheep_daily_water = cow_daily_water * 0.25

    # Calculate the total amount of water used daily
    total_water_daily = (num_cows * cow_daily_water) + (num_sheep * sheep_daily_water)

    # Calculate the total amount of water used weekly
    total_water_weekly = total_water_daily * 7

    # Display the total amount of water used weekly
    result = total_water_weekly
    return result

print(solution())