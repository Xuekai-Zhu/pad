def solution():
    """Kyle bikes for 2 hours to work every day. Ten times the time he takes to travel to work and back is the same as the cost of buying a pack of snacks (in dollars). How much will Ryan pay, in dollars, to buy 50 packs of snacks?"""
    # Define the time Kyle takes to travel to work and back
    time = 2 * 2 # 2 hours to work and 2 hours back

    # Calculate the cost of one pack of snacks
    snack_cost = time * 10

    # Calculate the total cost of 50 packs of snacks
    total_cost = snack_cost * 50

    # Display the total cost
    result = total_cost
    return result

print(solution())