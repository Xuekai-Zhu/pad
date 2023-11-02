def solution():
    """A certain tree was 100 meters tall at the end of 2017. It will grow 10% more than its previous height each year. How long has the tree grown from 2017 until the end of 2019?"""
    initial_height = 100
    growth_rate = 0.1
    years = 2
    final_height = initial_height*(1+growth_rate)**years
    growth = final_height - initial_height
    result = growth
    return result

print(solution())