def solution():
    # Total amount of money Carrie needs to save
    total_money_needed = 800 - 240  # cost of new iPhone subtracted by trade in value of Samsung Galaxy

    # Number of weeks Carrie needs to work
    weeks_to_work = total_money_needed / 80  # Carrie earns $80 per week from babysitting

    result = weeks_to_work
    return result

print(solution())