def solution():
    """For every one dozen flowers bought, a customer gets 2 free flowers. If Maria wants to buy 3 dozens flowers, how many pieces of flowers will she have in all?"""
    # Define the number of dozens Maria wants to buy
    dozens = 3

    # Calculate the total number of flowers
    total_flowers = dozens * 12

    # Calculate the number of free flowers Maria gets
    free_flowers = dozens * 2

    # Add the free flowers to the total
    total_flowers += free_flowers

    result = total_flowers
    return result

print(solution())