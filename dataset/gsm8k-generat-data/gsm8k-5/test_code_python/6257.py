def solution():
    morning_bags = 3  # Droid uses 3 bags of coffee beans in the morning
    afternoon_bags = morning_bags * 3  # Droid uses triple the morning number in the afternoon
    evening_bags = morning_bags * 2  # Droid uses twice the morning number in the evening
    bags_per_day = morning_bags + afternoon_bags + evening_bags  # Total bags of coffee beans used per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total bags of coffee beans used in a week
    total_bags = bags_per_day * days_per_week
    result = total_bags
    return result

print(solution())