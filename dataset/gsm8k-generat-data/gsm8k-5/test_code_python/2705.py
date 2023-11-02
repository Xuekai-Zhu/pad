def solution():
    initial_bill = 60  # Maximoff's initial monthly bill was $60
    increase_percentage = 30  # Maximoff's bill increased by 30% when he started working from home

    # Calculate the increased bill amount
    increased_amount = initial_bill * (increase_percentage/100)

    # Calculate the total monthly bill
    total_bill = initial_bill + increased_amount
    result = total_bill
    return result

print(solution())