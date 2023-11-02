def solution():
    # Calculate the number of eagle feathers Jerry has
    hawk_feathers = 6
    eagle_feathers = 17 * hawk_feathers

    # Calculate the total number of feathers and the remaining number of feathers after giving 10 to his sister
    total_feathers = hawk_feathers + eagle_feathers
    remaining_feathers = total_feathers - 10

    # Calculate the number of feathers Jerry sells
    sold_feathers = remaining_feathers // 2

    # Calculate the number of feathers Jerry has left
    feathers_left = remaining_feathers - sold_feathers
    result = feathers_left
    return result

print(solution())