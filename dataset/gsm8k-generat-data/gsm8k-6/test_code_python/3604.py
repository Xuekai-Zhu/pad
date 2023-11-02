def solution():
    # Calculate the total food donated by the people in the second week
    second_week_donation = 2 * 40  # donations were twice as high as the first week

    # Calculate the total food donated to the food bank
    total_donation = 40 + second_week_donation

    # Calculate the amount of food given to the homeless in the third week
    given_out = 0.7 * total_donation

    # Calculate the remaining amount of food in the food bank
    remaining_food = total_donation - given_out

    result = remaining_food
    return result

print(solution())