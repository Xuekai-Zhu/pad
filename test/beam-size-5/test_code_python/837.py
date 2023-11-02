def solution():
    
    # Define the cost of the car and phone
    CAR_COST = 10000
    PHONE_COST = 800

    # Define the initial amount of money Gabriel has
    initial_money = 5000

    # Define the amount of money Gabriel's brother gave him
    brother_money = 200

    # Calculate the total cost of the car and phone
    total_cost = CAR_COST + PHONE_COST

    # Calculate the amount of money Gabriel still needs
    remaining_money = total_cost - brother_money

    # Display the amount of money Gabriel still needs
    result = remaining_money
    return result

print(solution())