def solution():
    """Gillian’s phone bill is usually $50 a month. If the monthly bill increases by 10%, what will be her phone bill for the entire next year?"""
    # Define the initial bill amount and the percentage increase
    initial_bill = 50
    increase_percentage = 0.1

    # Calculate the new bill amount after the increase
    new_bill = initial_bill + (initial_bill * increase_percentage)

    # Calculate the total bill for the next year
    total_bill = new_bill * 12

    result = total_bill
    return result

print(solution())