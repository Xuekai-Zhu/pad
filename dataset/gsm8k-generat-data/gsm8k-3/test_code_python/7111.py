def solution():
    """Jerry finds six hawk feathers and 17 times as many eagle feathers as hawk feathers. If he gives 10 feathers to his sister and sells half the remaining feathers, how many does he have left?"""
    # Define the number of hawk feathers Jerry finds
    hawk_feathers = 6

    # Calculate the number of eagle feathers Jerry finds
    eagle_feathers = hawk_feathers * 17

    # Calculate the total number of feathers Jerry has
    total_feathers = hawk_feathers + eagle_feathers

    # Subtract the feathers given to his sister
    total_feathers -= 10

    # Calculate the number of feathers Jerry sells
    sold_feathers = total_feathers // 2

    # Calculate the number of feathers Jerry has left
    remaining_feathers = total_feathers - sold_feathers

    # Display the number of feathers Jerry has left
    result = remaining_feathers
    return result

print(solution())