def solution():
    """John decides to fix a racecar.  It cost $20,000 to fix but he gets a 20% discount.  He wins his first race but only keeps 90% of the money.  The prize is $70,000.  How much money did he make from the car?"""
    # Define the cost of the car fix
    FIX_COST = 20000

    # Calculate the discount he gets on the car fix
    discount = FIX_COST * 0.2

    # Calculate the actual cost of the car fix after the discount
    actual_fix_cost = FIX_COST - discount

    # Calculate the amount of money he wins from the race
    race_prize = 70000

    # Calculate the amount of money he keeps after winning the race
    money_kept = race_prize * 0.9

    # Calculate the total amount of money John made from the car
    total_money = money_kept - actual_fix_cost

    # Display the total amount of money John made
    result = total_money
    return result

print(solution())