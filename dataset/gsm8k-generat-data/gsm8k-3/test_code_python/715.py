def solution():
    """You start a business selling charm bracelets. You spend $1 on the string for each bracelet and $3 on beads for each bracelet. You sell the bracelets for $6 each. If you sell 25 bracelets, how much profit will you make?"""
    # Define the cost of string and beads for each bracelet
    STRING_COST = 1
    BEAD_COST = 3

    # Define the selling price of each bracelet
    SELLING_PRICE = 6

    # Define the number of bracelets sold
    num_bracelets = 25

    # Calculate the total cost of making the bracelets
    total_cost = num_bracelets * (STRING_COST + BEAD_COST)

    # Calculate the total revenue from selling the bracelets
    total_revenue = num_bracelets * SELLING_PRICE

    # Calculate the profit from selling the bracelets
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())