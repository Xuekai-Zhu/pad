def solution():
    """Méliès bought 2 kg of meat. The meat costs $82 per kilogram. Méliès has $180 in his wallet. How much money does he have left after paying for the meat?"""
    # Define the cost per kilogram of meat and the amount of meat bought
    MEAT_PRICE = 82
    AMOUNT_OF_MEAT = 2

    # Calculate the total cost of the meat
    total_cost = MEAT_PRICE * AMOUNT_OF_MEAT

    # Calculate the amount of money Méliès has left after paying for the meat
    money_left = 180 - total_cost

    # Display the amount of money Méliès has left
    result = money_left
    return result

print(solution())