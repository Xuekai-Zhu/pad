def solution():
    """Pauline will make tacos for dinner. She bought a box of taco shells that cost $5, 4 bell peppers that cost $1.5 each, and 2 pounds of meat that cost $3 per pound.  How much did she spend in all?"""
    # Define the cost of each item
    TACO_SHELLS_PRICE = 5
    BELL_PEPPER_PRICE = 1.5
    MEAT_PRICE = 3

    # Define the quantity of each item
    TACO_SHELLS_QUANTITY = 1
    BELL_PEPPER_QUANTITY = 4
    MEAT_QUANTITY = 2

    # Calculate the total cost of the taco shells
    taco_shells_cost = TACO_SHELLS_PRICE

    # Calculate the total cost of the bell peppers
    bell_pepper_cost = BELL_PEPPER_PRICE * BELL_PEPPER_QUANTITY

    # Calculate the total cost of the meat
    meat_cost = MEAT_PRICE * MEAT_QUANTITY

    # Calculate the total cost of all the items
    total_cost = taco_shells_cost + bell_pepper_cost + meat_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())