def solution():
    """It's Yvette's turn to treat herself and her three best friends to a round of ice cream sundaes.  Alicia orders the peanut butter sundae for $7.50.  Brant orders the Royal banana split sundae for $10.00.  Josh orders the death by chocolate sundae for $8.50 and Yvette orders the cherry jubilee sundae for $9.00.  She leaves her waiter a 20% tip.  How much will her final bill be?"""
    # Define the prices of each sundae
    peanut_butter_price = 7.5
    banana_split_price = 10
    chocolate_price = 8.5
    cherry_price = 9

    # Calculate the total cost of the sundaes
    total_cost = peanut_butter_price + banana_split_price + chocolate_price + cherry_price

    # Calculate the tip amount
    tip = total_cost * 0.2

    # Calculate the final bill
    final_bill = total_cost + tip

    # Display the final bill
    result = final_bill
    return result

print(solution())