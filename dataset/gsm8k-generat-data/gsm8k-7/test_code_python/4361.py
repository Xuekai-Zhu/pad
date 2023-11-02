def solution():
    total_legs = 20
    legs_per_tripodasaurus = 3

    # Calculate the total number of tripodasauruses based on their legs
    num_tripodasauruses = total_legs // legs_per_tripodasaurus
    result = num_tripodasauruses
    return result

print(solution())