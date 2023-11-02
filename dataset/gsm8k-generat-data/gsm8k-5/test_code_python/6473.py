def solution():
    # Calculate the number of candies Bobby eats during the weekdays
    candies_weekdays = 2 * 5

    # Calculate the number of candies Bobby eats during the remaining days
    candies_remaining_days = 1 * 2

    # Calculate the total number of candies Bobby eats in a week
    candies_per_week = candies_weekdays + candies_remaining_days

    # Calculate the total number of candies Bobby eats in 3 weeks
    candies_3_weeks = candies_per_week * 3

    # Calculate the number of candies in a packet
    candies_per_packet = candies_3_weeks / 2
    result = candies_per_packet
    return result

print(solution())