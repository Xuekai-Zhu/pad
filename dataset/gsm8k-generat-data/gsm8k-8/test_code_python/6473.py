def solution():
    # Define the total number of days
    total_days = 21

    # Calculate the total number of candies Bobby eats during the weekdays
    weekday_candies = 2 * 5

    # Calculate the total number of candies he takes during the weekends
    weekend_candies = 1 * 2

    # Define the total number of candies in two packets
    total_candies = weekday_candies * 2 + weekend_candies * 2

    # Calculate the number of candies in a single packet
    candies_in_packet = total_candies / 2 / 3

    result = candies_in_packet
    return result

print(solution())