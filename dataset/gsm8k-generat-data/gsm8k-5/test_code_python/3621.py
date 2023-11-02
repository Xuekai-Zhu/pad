def solution():
    fiona_hours = 40 # Fiona worked for 40 hours a week
    john_hours = 30 # John worked for 30 hours a week
    jeremy_hours = 25 # Jeremy worked for 25 hours a week
    wage_per_hour = 20 # Their boss pays $20 per hour

    # Calculate the total cost of wages paid out by the boss every month
    total_wages = (fiona_hours + john_hours + jeremy_hours) * wage_per_hour * 4 # Multiply by 4 weeks in a month

    result = total_wages
    return result

print(solution())