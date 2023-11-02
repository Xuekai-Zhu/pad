def solution():
    """Three friends ate a total of 8 pounds of fruit. Mario had 8 ounces of oranges, while Lydia ate 24 ounces of apples. Nicolai ate peaches. How many pounds of peaches did Nicolai eat?"""
    # Define the total weight of fruit as 8 pounds
    total_weight = 8

    # Convert the weight of Mario's oranges and Lydia's apples from ounces to pounds
    mario_oranges = 8 / 16
    lydia_apples = 24 / 16

    # Calculate the weight of peaches by subtracting the weights of Mario's oranges and Lydia's apples from the total weight
    peach_weight = total_weight - mario_oranges - lydia_apples

    # Return the weight of peaches as the result
    result = peach_weight
    return result

print(solution())