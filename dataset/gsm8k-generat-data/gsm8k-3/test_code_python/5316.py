def solution():
    """Shane prepares sandwiches for the Boy Scouts. He buys 2 packages of sliced bread containing 20 slices each, and he also buys 2 packages of sliced ham containing 8 slices each. Shane will make as many sandwiches as he can according to the ham he has. How many slices of bread will he have leftover?"""
    # Define the number of slices of bread and ham per package
    BREAD_PER_PACK = 20
    HAM_PER_PACK = 8

    # Calculate the total number of slices of bread and ham purchased
    total_bread = 2 * BREAD_PER_PACK
    total_ham = 2 * HAM_PER_PACK

    # Calculate the maximum number of sandwiches that can be made
    max_sandwiches = total_ham // 2

    # Calculate the number of slices of bread used for the sandwiches
    bread_for_sandwiches = max_sandwiches * 2

    # Calculate the number of slices of bread leftover
    bread_leftover = total_bread - bread_for_sandwiches

    # Display the number of slices of bread leftover
    result = bread_leftover
    return result

print(solution())