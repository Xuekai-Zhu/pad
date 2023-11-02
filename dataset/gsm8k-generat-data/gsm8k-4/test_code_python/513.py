def solution():
    """Jennifer has ten pears, 20 oranges, and twice as many apples as pears. If she gives her sister two of each fruit, how many fruits does she have left?"""
    # Define the initial number of fruits
    pears = 10
    oranges = 20
    apples = pears * 2

    # Subtract the fruits given to sister
    pears -= 2
    oranges -= 2
    apples -= 2

    # Calculate the total number of fruits left
    total_fruits = pears + oranges + apples

    result = total_fruits
    return result

print(solution())