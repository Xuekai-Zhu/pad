def solution():
    """Cheyenne is a craftswoman making pots for sale. On a particular week, she made 80 clay pots. However, when she put them in the sun to dry, 2/5 of the pots cracked and could not be sold. How much money did Cheyenne make from selling the remaining items at $40 per clay pot?"""
    # Define the number of pots made
    total_pots = 80

    # Calculate the number of pots that cracked
    cracked_pots = total_pots * (2/5)

    # Calculate the number of pots that could be sold
    sold_pots = total_pots - cracked_pots

    # Calculate the total amount of money from selling the pots
    total_money = sold_pots * 40

    # return the result
    result = total_money
    return result

print(solution())