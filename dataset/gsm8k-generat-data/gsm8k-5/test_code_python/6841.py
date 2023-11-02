def solution():
    vitamins_per_day = 2  # Janet takes 2 multivitamins per day
    calcium_supplements_per_day = 3  # Janet takes 3 calcium supplements per day for the first 2 weeks
    calcium_supplements_per_day_low = 1  # Janet takes 1 calcium supplement per day for the last 2 weeks
    days_in_month = 30  # Assuming there are 30 days in the month

    # Calculate the total number of pills Janet takes for the first 2 weeks
    pills_first_half = (vitamins_per_day + calcium_supplements_per_day) * 14

    # Calculate the total number of pills Janet takes for the last 2 weeks
    pills_second_half = (vitamins_per_day + calcium_supplements_per_day_low) * 14

    # Calculate the total number of pills Janet takes in the month
    total_pills = pills_first_half + pills_second_half
    result = total_pills
    return result

print(solution())