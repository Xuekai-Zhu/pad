def solution():
    # Calculate the number of feathers pulled out
    feathers_pulled_out = 2 * 23

    # Calculate the number of feathers the chicken has left
    feathers_left = 5263 - feathers_pulled_out

    # Calculate the total number of feathers after both road crossings
    total_feathers = feathers_left - feathers_pulled_out + feathers_left

    result = total_feathers
    return result

print(solution())