def solution():
    lion_consumption = 25  # Lion consumes 25 kg of meat per day
    tiger_consumption = 20  # Tiger consumes 20 kg of meat per day
    total_meat = 90  # They have a total of 90 kg of meat

    # Calculate the total consumption per day
    total_consumption = lion_consumption + tiger_consumption

    # Calculate the number of days the meat will last
    days = total_meat / total_consumption
    result = days
    return result

print(solution())