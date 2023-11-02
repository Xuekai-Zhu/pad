def solution():
    total_gallons = 105  # Flora needs to drink 105 gallons of milk in 3 weeks
    weeks = 3  # Flora has 3 weeks to drink the milk
    gallons_per_day = 3  # Flora currently drinks 3 gallons of milk per day

    # Calculate the total gallons Flora will drink in 3 weeks at her current rate
    total_gallons_drunk = gallons_per_day * 7 * weeks

    # Calculate how many more gallons Flora needs to drink per day to meet Dr. Juan's requirement
    extra_gallons_per_day = (total_gallons - total_gallons_drunk) / (7 * weeks)
    result = extra_gallons_per_day
    return result

print(solution())