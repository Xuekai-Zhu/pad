def solution():
    """Janelle had 26 green marbles. Then she bought 6 bags of blue marbles. There were 10 marbles in each bag. She created a gift of 6 green marbles and 8 blue marbles and gave it to a friend. How many marbles does Janelle have now?"""
    # Define the initial number of green marbles
    green_marbles = 26

    # Define the number of bags of blue marbles purchased and the number of marbles in each bag
    blue_bags = 6
    blue_marbles_per_bag = 10

    # Calculate the total number of blue marbles purchased
    blue_marbles = blue_bags * blue_marbles_per_bag

    # Calculate the total number of marbles before the gift
    total_marbles = green_marbles + blue_marbles

    # Subtract the gift marbles
    total_marbles -= 6 + 8

    # Return the result
    result = total_marbles
    return result

print(solution())