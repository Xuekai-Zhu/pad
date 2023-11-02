def solution():
    first_week_donation = 40  # 40 pounds of food were donated in the first week
    second_week_donation = 2 * first_week_donation  # Second week donations were twice as high as the first week
    total_donation = first_week_donation + second_week_donation
    distributed_food = 0.7 * total_donation  # 70% of the donated food was given out to the homeless
    remaining_food = total_donation - distributed_food
    result = remaining_food
    return result

print(solution())