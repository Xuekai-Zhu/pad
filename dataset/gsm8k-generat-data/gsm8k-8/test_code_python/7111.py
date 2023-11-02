def solution():
    # Define the number of hawk feathers and eagle feathers
    hawk_feathers = 6
    eagle_feathers = 17 * hawk_feathers

    # Calculate the total number of feathers
    total_feathers = hawk_feathers + eagle_feathers

    # Substract 10 feathers given to his sister
    remaining_feathers = total_feathers - 10

    # Calculate the number of feathers he sells
    feathers_sold = remaining_feathers / 2

    # Calculate the number of feathers he has left
    feathers_left = remaining_feathers - feathers_sold
    result = feathers_left
    return result

print(solution())