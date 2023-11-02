def solution():
    first_week_donation = 40
    second_week_donation = 2 * first_week_donation
    third_week_donation = 0.3 * (first_week_donation + second_week_donation)

    # Calculate the total donated food
    total_donation = first_week_donation + second_week_donation + third_week_donation

    # Calculate the amount of food given out to the homeless
    donated_to_homeless = 0.7 * total_donation

    # Calculate the amount of remaining food in the food bank
    remaining_food = total_donation - donated_to_homeless

    result = remaining_food
    return result

print(solution())