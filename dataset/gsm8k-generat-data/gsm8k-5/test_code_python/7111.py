def solution():
    # Calculate the number of eagle feathers
    hawk_feathers = 6
    eagle_feathers = hawk_feathers * 17

    # Calculate the total number of feathers
    total_feathers = hawk_feathers + eagle_feathers

    # Give 10 feathers to Jerry's sister
    total_feathers -= 10

    # Sell half the remaining feathers
    remaining_feathers = total_feathers // 2

    result = remaining_feathers
    return result

print(solution())