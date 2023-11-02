def solution():
    lion_meat = 25  # kilograms of meat consumed by a lion per day
    tiger_meat = 20  # kilograms of meat consumed by a tiger per day
    total_meat = 90  # total kilograms of meat available

    # Calculate the number of days the meat will last
    days = total_meat / (lion_meat + tiger_meat)
    result = days
    return result

print(solution())