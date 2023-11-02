def solution():
    """There are six oranges in a fruit basket. There are two fewer apples than oranges. There are 3 times as many bananas as apples, and there are half as many peaches as bananas. How many pieces of fruit are in the fruit basket?"""
    # Define the initial number of oranges
    oranges = 6

    # Calculate the number of apples
    apples = oranges - 2

    # Calculate the number of bananas
    bananas = 3 * apples

    # Calculate the number of peaches
    peaches = bananas / 2

    # Calculate the total number of pieces of fruit
    total_fruit = oranges + apples + bananas + peaches

    # return the result
    result = total_fruit
    return result

print(solution())