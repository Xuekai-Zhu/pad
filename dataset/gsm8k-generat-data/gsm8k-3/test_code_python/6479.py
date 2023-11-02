def solution():
    """Cheyenne is a craftswoman making pots for sale. On a particular week, she made 80 clay pots. However, when she put them in the sun to dry, 2/5 of the pots cracked and could not be sold. How much money did Cheyenne make from selling the remaining items at $40 per clay pot?"""
    # Define the number of pots made and the fraction that cracked
    total_pots = 80
    cracked_fraction = 2/5

    # Calculate the number of pots that did not crack
    good_pots = total_pots * (1 - cracked_fraction)

    # Calculate the total amount of money Cheyenne made
    total_money = good_pots * 40

    # Display the total amount of money
    result = total_money
    return result

print(solution())