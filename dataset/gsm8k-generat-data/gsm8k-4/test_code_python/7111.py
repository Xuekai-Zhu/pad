def solution():
    """Jerry finds six hawk feathers and 17 times as many eagle feathers as hawk feathers. If he gives 10 feathers to his sister and sells half the remaining feathers, how many does he have left?"""
    # Define the number of hawk feathers found
    hawk_feathers = 6

    # Define the number of eagle feathers found
    eagle_feathers = hawk_feathers * 17

    # Calculate the total number of feathers
    total_feathers = hawk_feathers + eagle_feathers

    # Subtract 10 feathers for his sister
    total_feathers -= 10

    # Calculate the number of feathers he sells
    feathers_sold = total_feathers / 2

    # Calculate the number of feathers he has left
    feathers_left = total_feathers - feathers_sold

    # return the result
    result = feathers_left
    return result

print(solution())