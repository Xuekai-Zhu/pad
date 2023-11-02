def solution():
    """There are 3 ducks in a pond and they all eat some pieces of bread thrown in the water. One duck eats half of all the pieces of bread. Another duck eats only 13 pieces of the bread and the last duck eats 7 pieces of bread. There are 30 pieces of bread left in the water, how many total pieces of bread were thrown in the pond?"""
    # Define the number of pieces of bread eaten by the first duck
    duck_1 = None

    # Define the number of pieces of bread eaten by the second duck
    duck_2 = 13

    # Define the number of pieces of bread eaten by the third duck
    duck_3 = 7

    # Calculate the total number of pieces of bread eaten
    total_eaten = duck_1 + duck_2 + duck_3

    # Calculate the number of pieces of bread left in the water
    left_in_water = 30

    # Calculate the total number of pieces of bread thrown in the pond
    total_thrown = total_eaten + left_in_water

    result = total_thrown
    return result

print(solution())