def solution():
    """Méliès bought 2 kg of meat. The meat costs $82 per kilogram. Méliès has $180 in his wallet. How much money does he have left after paying for the meat?"""
    # Define the price of the meat and the initial amount of money in the wallet
    price_per_kg = 82
    initial_money = 180

    # Calculate the total cost of the meat
    total_cost = price_per_kg * 2

    # Calculate the amount of money left after paying for the meat
    money_left = initial_money - total_cost

    # return the result
    result = money_left
    return result

print(solution())