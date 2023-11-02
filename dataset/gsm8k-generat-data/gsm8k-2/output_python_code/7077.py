def solution():
    """There are 3 ducks in a pond and they all eat some pieces of bread thrown in the water. One duck eats half of all the pieces of bread. Another duck eats only 13 pieces of the bread and the last duck eats 7 pieces of bread. There are 30 pieces of bread left in the water, how many total pieces of bread were thrown in the pond?"""
    remaining_bread = 30
    third_duck_bread = 7
    second_duck_bread = 13
    half_bread = (remaining_bread + third_duck_bread + second_duck_bread) * 2
    total_bread = remaining_bread + half_bread + third_duck_bread + second_duck_bread
    result = total_bread
    return result

print(solution())