def solution():
    
    # Define the cost of adult and child tickets
    ADULT_COST = 12
    CHILD_COST = 10

    # Define the amount of change received
    CHANGE_AMOUNT = 8

    # Calculate the total cost of tickets
    total_cost = ADULT_COST + CHILD_COST

    # Calculate the amount of money Brittany's mom gave the cashier
    cashier_money = total_cost + CHANGE_AMOUNT

    # Display the amount of money Brittany's mom gave the cashier
    result = cashier_money
    return result

print(solution())