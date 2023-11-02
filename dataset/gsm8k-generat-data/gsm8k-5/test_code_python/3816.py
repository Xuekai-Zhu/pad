def solution():
    pay_rate = 5  # Goldie makes $5 an hour for pet-sitting
    hours_week1 = 20  # Goldie worked for 20 hours in the first week
    hours_week2 = 30  # Goldie worked for 30 hours in the second week

    # Calculate the total pay for the two weeks
    total_pay = (pay_rate * hours_week1) + (pay_rate * hours_week2)
    result = total_pay
    return result

print(solution())