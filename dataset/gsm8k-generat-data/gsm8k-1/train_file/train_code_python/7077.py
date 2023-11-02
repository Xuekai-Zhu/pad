def solution():
    """There are 3 ducks in a pond and they all eat some pieces of bread thrown in the water. One duck eats half of all the pieces of bread. Another duck eats only 13 pieces of the bread and the last duck eats 7 pieces of bread. There are 30 pieces of bread left in the water, how many total pieces of bread were thrown in the pond?"""
    bread_left = 30
    duck1 = bread_left * 2
    duck2 = 13
    duck3 = 7
    total_bread = duck1 + duck2 + duck3 + bread_left
    result = total_bread
    return result

print(solution())