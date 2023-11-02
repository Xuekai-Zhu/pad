def solution():
    """Opal won $100.00 betting on a horse race.  She put half of her winnings into savings and bet the other half of her winnings.  This time, she made a 60% profit and again, put half of her earnings into savings.  How much did she put into her savings?"""
    # Define Opal's initial winnings and calculate the amount she put into savings
    initial_winnings = 100
    savings1 = initial_winnings / 2

    # Calculate Opal's second winnings and the amount she put into savings again
    second_winnings = initial_winnings / 2 * 1.6
    savings2 = second_winnings / 2

    # Add up the total amount Opal put into savings
    total_savings = savings1 + savings2

    # Display the total savings amount
    result = total_savings
    return result

print(solution())