def solution():
    """Carl caused a car accident that resulted in $40,000 worth of property damage and $70,000 worth of medical bills. If Carl's insurance company will pay 80% of the costs, leaving Carl to pay the remaining 20%, how much does Carl personally owe?"""
    # Calculate the total cost of the accident
    total_cost = 40000 + 70000

    # Calculate how much Carl's insurance will pay
    insurance_payment = total_cost * 0.8

    # Calculate how much Carl personally owes
    carl_owes = total_cost - insurance_payment

    # Display how much Carl owes
    result = carl_owes
    return result

print(solution())