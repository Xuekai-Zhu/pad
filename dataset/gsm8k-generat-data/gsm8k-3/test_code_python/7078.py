def solution():
    """There are 3 ducks in a pond and they all eat some pieces of bread thrown in the water. One duck eats half of all the pieces of bread. Another duck eats only 13 pieces of the bread and the last duck eats 7 pieces of bread. There are 30 pieces of bread left in the water, how many total pieces of bread were thrown in the pond?"""
    # Define the number of pieces of bread eaten by each duck
    duck1 = 0.5
    duck2 = 13
    duck3 = 7

    # Calculate the total number of pieces of bread eaten
    total_eaten = duck1 + duck2 + duck3

    # Calculate the initial number of pieces of bread
    initial_bread = total_eaten + 30

    # Convert the initial number of pieces of bread to an integer
    total_bread = int(initial_bread)

    # Display the total number of pieces of bread thrown in the pond
    result = total_bread
    return result

print(solution())