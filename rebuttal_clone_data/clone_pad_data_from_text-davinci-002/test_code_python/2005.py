def solution():
    cups_sold_to_construction_crew = 1/2
    cups_sold_to_kids = 18
    cups_given_away = cups_sold_to_kids / 2
    cups_consumed = 1
    total_cups = cups_sold_to_construction_crew + cups_sold_to_kids + cups_given_away + cups_consumed
    result = total_cups
    return result

print(solution())