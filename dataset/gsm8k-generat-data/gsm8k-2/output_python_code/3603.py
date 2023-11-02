def solution():
    """Lyanna set up a food bank to collect food to give to the homeless in her local town. In the first week, 40 pounds of food were donated to the food bank by the people of her local town. In the second week, donations were twice as high as the first week. If she gave out 70% of the donated food to the homeless in the third week, calculate the amount of food remaining in the food bank."""
    first_week_donation = 40
    second_week_donation = 2 * first_week_donation
    total_donation = first_week_donation + second_week_donation
    donated_to_homeless = 0.7 * total_donation
    remaining_food = total_donation - donated_to_homeless
    result = remaining_food
    return result

print(solution())