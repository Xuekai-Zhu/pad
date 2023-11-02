def solution():
    """Jennifer has ten pears, 20 oranges, and twice as many apples as pears. If she gives her sister two of each fruit, how many fruits does she have left?"""
    # Define the number of pears, oranges, and apples
    pears = 10
    oranges = 20
    apples = pears * 2

    # Define the number of fruits given to Jennifer's sister
    sister_fruits = 2 + 2 + 2 * 2  # Two pears, two oranges, and two apples

    # Calculate the number of fruits Jennifer has left
    remaining_fruits = pears + oranges + apples - sister_fruits

    # Display the number of fruits Jennifer has left
    result = remaining_fruits
    return result

print(solution())