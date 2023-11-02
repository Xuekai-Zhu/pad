def solution():
    packets_of_candy = 2
    days_per_week = 7
    candies_per_weekday = 2
    candies_per_weekend_day = 1
    total_weeks = 3

    # Calculate the total number of candies Bobby eats each week
    candies_per_week = (candies_per_weekday * 5) + (candies_per_weekend_day * 2)

    # Calculate the total number of candies Bobby eats in 3 weeks
    total_candies = total_weeks * candies_per_week

    # Calculate the number of candies in each packet
    candies_per_packet = total_candies / packets_of_candy
    result = candies_per_packet
    return result

print(solution())