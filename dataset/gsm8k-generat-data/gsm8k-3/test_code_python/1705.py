def solution():
    """For every one dozen flowers bought, a customer gets 2 free flowers. If Maria wants to buy 3 dozens flowers, how many pieces of flowers will she have in all?"""
    # Define the number of dozens of flowers Maria wants to buy
    dozens = 3

    # Calculate the total number of flowers Maria will receive, accounting for the free flowers
    total_flowers = dozens * 12 + dozens * 2

    # Display the total number of flowers Maria will have
    result = total_flowers
    return result

print(solution())