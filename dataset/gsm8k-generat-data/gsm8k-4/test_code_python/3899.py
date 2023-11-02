def solution():
    """There are 56 pieces of fruit in a box. One-fourth of the box contains oranges. There are half as many peaches as oranges and five times as many apples as peaches. How many apples are in the box?"""
    # Define the total number of fruit in the box
    total_fruit = 56

    # Calculate the number of oranges in the box
    oranges = total_fruit / 4

    # Calculate the number of peaches in the box
    peaches = oranges / 2

    # Calculate the number of apples in the box
    apples = peaches * 5

    result = apples
    return result

print(solution())