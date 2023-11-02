def solution():
    """Jackson is making pancakes with three ingredients: flour, milk and eggs. 20% of the bottles of milk are spoiled and the rest are fresh. 60% of the eggs are rotten. 1/4 of the cannisters of flour have weevils in them. If Jackson picks a bottle of milk, an egg and a canister of flour at random, what are the odds all three ingredients will be good?"""
    
    # Calculate the probability that a bottle of milk is fresh
    p_fresh_milk = 0.8

    # Calculate the probability that an egg is not rotten
    p_good_egg = 0.4

    # Calculate the probability that a canister of flour does not have weevils
    p_good_flour = 0.75

    # Calculate the probability that all three ingredients are good
    p_all_good = p_fresh_milk * p_good_egg * p_good_flour

    # Display the probability rounded to 2 decimal places
    result = round(p_all_good, 2)
    return result

print(solution())