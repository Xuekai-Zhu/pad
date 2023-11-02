def solution():
    # Calculate the total number of hours worked by the two men
    total_hours = 10 + 8 + 15  # 10 hours worked on the first day, 8 hours on the second, and 15 hours on the third

    # Calculate the total amount of money paid to both men
    total_payment = total_hours * 10 * 2  # each man is paid $10 for every hour of work, and there are two men working
    result = total_payment
    return result

print(solution())