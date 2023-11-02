def solution():
    daily_passengers = 1200000  # The bus system carries 1,200,000 people each day
    weeks = 13  # The bus system wants to know how many people it will carry in 13 weeks

    # Calculate the total number of passengers the bus system will carry in 13 weeks
    total_passengers = daily_passengers * 7 * weeks

    result = total_passengers
    return result

print(solution())