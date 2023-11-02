def solution():
    """Natalie has $26 to go shopping. She bought a jumper for $9, a T-shirt for $4, and a pair of heels for $5. How much money does Natalie have left?"""
    # Define the initial amount of money Natalie has
    initial_money = 26

    # Define the cost of the items Natalie bought
    jumper_cost = 9
    tshirt_cost = 4
    heels_cost = 5

    # Calculate the total cost of the items Natalie bought
    total_cost = jumper_cost + tshirt_cost + heels_cost

    # Calculate the amount of money Natalie has left
    money_left = initial_money - total_cost

    # Display the amount of money Natalie has left
    result = money_left
    return result

print(solution())