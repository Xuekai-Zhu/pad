def solution():
    num_shirts = 4
    num_pants = num_shirts * 2
    num_shorts = num_pants / 2

    # Calculate the total number of pieces of clothing
    total_clothes = num_shirts + num_pants + num_shorts
    result = total_clothes
    return result

print(solution())