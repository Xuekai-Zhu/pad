def solution():
    """After eating half of the number of fruits he had, Martin remained with twice as many oranges as limes. If he has 50 oranges now, how many fruits did he initially have?"""
    # Let's assume Martin initially had "x" fruits
    # After eating half of them, he has "x/2" fruits left
    # Let's assume he had "y" limes initially
    # Since he has twice as many oranges as limes left, he now has "2y" oranges
    # So, we have "2y = 50", which means "y = 25"
    # And we also have "x/2 = (y + 2y)", which simplifies to "x/2 = 3y"
    # Substituting the value of y, we get "x/2 = 75"
    # Solving for x, we get "x = 150"

    initial_fruits = 150
    result = initial_fruits
    return result

print(solution())