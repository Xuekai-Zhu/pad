def solution():
    cups_of_basil_for_1_cup_of_pesto = 4
    weekly_basil_harvest = 16
    weeks_of_harvest = 8

    # Calculate total cups of basil harvested
    total_basil_harvest = weekly_basil_harvest * weeks_of_harvest

    # Calculate total cups of pesto that can be made
    total_cups_of_pesto = total_basil_harvest // cups_of_basil_for_1_cup_of_pesto

    result = total_cups_of_pesto
    return result

print(solution())