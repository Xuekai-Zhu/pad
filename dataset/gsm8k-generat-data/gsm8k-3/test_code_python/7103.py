def solution():
    """Harry decided to buy some balloons for his friend's birthday party. One balloon costs $0.5, and a pack of 10 balloons is cheaper and costs only $3. Finally, Harry wants to bring to the party exactly 14 balloons. How much did he need to pay for them?"""
    # Define the prices for individual and pack of balloons
    SINGLE_BALLOON_PRICE = 0.5
    PACK_PRICE = 3
    PACK_SIZE = 10

    # Calculate the number of individual balloons and packs needed
    packs_needed = 14 // PACK_SIZE
    single_balloons_needed = 14 % PACK_SIZE

    # Calculate the total cost of the balloons
    total_cost = packs_needed * PACK_PRICE
    total_cost += single_balloons_needed * SINGLE_BALLOON_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())