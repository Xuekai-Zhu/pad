def solution():
    hawk_feathers = 6
    eagle_feathers = 17 * hawk_feathers
    total_feathers = hawk_feathers + eagle_feathers
    feathers_gone = 10

    # Calculate the number of feathers Jerry has left after giving some to his sister
    feathers_left = total_feathers - feathers_gone

    # Calculate the number of feathers Jerry sells
    feathers_sold = feathers_left / 2

    # Calculate the number of feathers Jerry has left after selling half
    feathers_left = feathers_left - feathers_sold
    result = feathers_left
    return result

print(solution())