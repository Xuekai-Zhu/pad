def solution():
    """Hakeem has always loved artichoke dip and plans to make it this weekend. He has $15 dollars to buy artichokes and can find the rest of the ingredients at home. It takes 3 artichokes to make 5 ounces of dip. How many ounces can he make if artichokes cost $1.25 each?"""
    # Define the cost and number of available artichokes
    ARTICHOKE_COST = 1.25
    AVAILABLE_ARTICHOKES = 15 / ARTICHOKE_COST

    # Define the number of artichokes needed for 5 ounces of dip
    ARTICHOKES_PER_DIP = 3
    OUNCES_PER_DIP = 5

    # Calculate the maximum number of dips that can be made with available artichokes
    max_dips = AVAILABLE_ARTICHOKES // ARTICHOKES_PER_DIP

    # Calculate the total number of ounces of dip that can be made
    total_ounces = max_dips * OUNCES_PER_DIP

    # Display the total number of ounces of dip that can be made
    result = total_ounces
    return result

print(solution())