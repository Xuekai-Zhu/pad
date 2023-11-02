def solution():
    # Define the original monthly bill and the percentage increase
    original_bill = 60
    percentage_increase = 30/100

    # Calculate the new monthly bill with the increase
    new_bill = original_bill + (original_bill * percentage_increase)

    # Return the new monthly bill
    result = new_bill
    return result

print(solution())