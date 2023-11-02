def solution():
    """Jackson is making pancakes with three ingredients: flour, milk and eggs. 20% of the bottles of milk are spoiled and the rest are fresh. 60% of the eggs are rotten. 1/4 of the cannisters of flour have weevils in them. If Jackson picks a bottle of milk, an egg and a canister of flour at random, what are the odds all three ingredients will be good?"""
    fresh_milk_prob = 0.8
    fresh_eggs_prob = 0.4
    fresh_flour_prob = 0.75
    odds = fresh_milk_prob * fresh_eggs_prob * fresh_flour_prob
    result = odds
    return result

print(solution())