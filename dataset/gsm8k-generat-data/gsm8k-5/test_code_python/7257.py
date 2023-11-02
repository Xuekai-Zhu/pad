def solution():
    beef = 20  # James buys 20 pounds of beef
    pork = beef / 2  # James buys half as much pork as beef
    total_meat = beef + pork  # Total amount of meat James buys
    meals = total_meat / 1.5  # Number of meals James can make with the total amount of meat
    revenue = meals * 20  # James sells each meal for $20

    result = revenue
    return result

print(solution())