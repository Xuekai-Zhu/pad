def solution():
    """There are 56 pieces of fruit in a box. One-fourth of the box contains oranges. There are half as many peaches as oranges and five times as many apples as peaches. How many apples are in the box?"""
    # Calculate the number of oranges in the box
    oranges = 56 / 4

    # Calculate the number of peaches in the box
    peaches = oranges / 2

    # Calculate the number of apples in the box
    apples = peaches * 5

    # Display the number of apples
    result = apples
    return result

print(solution())