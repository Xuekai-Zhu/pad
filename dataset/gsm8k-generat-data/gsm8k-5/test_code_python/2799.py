def solution():
    remaining_debt = 100 - 40  # Jake still owes $60
    wage_per_hour = 15  # Jake earns $15 per hour

    # Calculate the number of hours Jake has to work to pay off the remaining debt
    hours_worked = remaining_debt / wage_per_hour
    result = hours_worked
    return result

print(solution())