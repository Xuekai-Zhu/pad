def solution():
    """Lyanna set up a food bank to collect food to give to the homeless in her local town. In the first week, 40 pounds of food were donated to the food bank by the people of her local town. In the second week, donations were twice as high as the first week. If she gave out 70% of the donated food to the homeless in the third week, calculate the amount of food remaining in the food bank."""
    # Define the initial donation
    week1_donation = 40

    # Calculate the donation for the second week
    week2_donation = 2 * week1_donation

    # Calculate the total donations
    total_donation = week1_donation + week2_donation

    # Calculate the amount of food given to the homeless in the third week
    donated_food = total_donation * 0.7

    # Calculate the amount of food remaining in the food bank
    remaining_food = total_donation - donated_food

    result = remaining_food
    return result

print(solution())