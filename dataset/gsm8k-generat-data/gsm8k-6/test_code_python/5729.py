def solution():
    # Calculate the number of feathers Milly needs in total
    total_feathers = 12 * 200  # 12 boas with 200 feathers each

    # Calculate the number of feathers she can safely pluck from each flamingo
    safe_feathers = 0.25 * 20  # can only pluck 25% of 20 tail feathers

    # Calculate the number of flamingos she needs to harvest
    num_flamingos = total_feathers / safe_feathers

    result = num_flamingos
    return result

print(solution())