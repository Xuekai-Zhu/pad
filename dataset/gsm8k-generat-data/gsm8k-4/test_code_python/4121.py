def solution():
    """Jackson is making pancakes with three ingredients: flour, milk and eggs. 20% of the bottles of milk are spoiled and the rest are fresh. 60% of the eggs are rotten. 1/4 of the canisters of flour have weevils in them. If Jackson picks a bottle of milk, an egg and a canister of flour at random, what are the odds all three ingredients will be good?"""
    # Define the proportion of good and bad milk bottles
    good_milk = 0.8
    bad_milk = 0.2

    # Define the proportion of good and bad eggs
    good_eggs = 0.4
    bad_eggs = 0.6

    # Define the proportion of good and bad flour canisters
    good_flour = 0.75
    bad_flour = 0.25

    # Calculate the probability of getting all good ingredients
    probability = good_milk * good_eggs * good_flour

    # Return the result as a percentage
    result = probability * 100
    return result

print(solution())