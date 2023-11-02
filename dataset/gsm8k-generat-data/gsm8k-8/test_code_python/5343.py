def solution():
    # Define the initial bill and the percentage increase
    initial_bill = 50
    percentage_increase = 0.1

    # Calculate the new monthly bill
    new_bill = initial_bill + (initial_bill * percentage_increase)

    # Calculate the annual bill
    annual_bill = new_bill * 12
    result = annual_bill
    return result

print(solution())