def solution():
    
    # Define the prices and quantities of Parmesan and Mozzarella cheese
    PARMESAN_PRICE = 11
    MOZZARELLA_PRICE = 6
    PARMESAN_QUANTITY = 2
    MOZZARELLA_QUANTITY = 3

    # Calculate the total cost of the meat
    total_cost = (PARMESAN_PRICE * PARMESAN_QUANTITY) + (MOZZARELLA_PRICE * MOZZARELLA_QUANTITY)

    # Calculate the amount of money Amor will have left after buying meat
    remaining_money = 50 - total_cost

    # Display the remaining money
    result = remaining_money
    return result

print(solution())