def solution():
    """Gloria wants to buy the $129,000 mountain cabin that her friend Alfonso is selling. She only has $150 in cash. She intends to raise the remaining amount by selling her mature trees for lumber. She has 20 cypress trees, 600 pine trees, and 24 maple trees. She will get $100 for each cypress tree, $300 for a maple tree, and $200 per pine tree. After paying Alfonso for the cabin, how much money will Gloria have left?"""
    # Define the cost of the mountain cabin and the initial amount Gloria has
    cabin_cost = 129000
    gloria_initial = 150

    # Calculate the amount Gloria will earn from selling her trees
    cypress_earnings = 20 * 100
    pine_earnings = 600 * 200
    maple_earnings = 24 * 300
    total_earnings = cypress_earnings + pine_earnings + maple_earnings

    # Calculate the amount Gloria will have left after buying the cabin
    gloria_left = gloria_initial + total_earnings - cabin_cost

    # Return the result
    result = gloria_left
    return result

print(solution())