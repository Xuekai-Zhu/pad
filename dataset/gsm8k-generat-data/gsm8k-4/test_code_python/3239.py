def solution():
    """Carl caused a car accident that resulted in $40,000 worth of property damage and $70,000 worth of medical bills. If Carl's insurance company will pay 80% of the costs, leaving Carl to pay the remaining 20%, how much does Carl personally owe?"""
    # Define the total cost of the accident
    total_cost = 40000 + 70000

    # Calculate the amount paid by the insurance company
    insurance_payment = total_cost * 0.8

    # Calculate the amount owed by Carl
    carl_payment = total_cost - insurance_payment

    # Return the result
    result = carl_payment
    return result

print(solution())