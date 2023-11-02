def solution():
    # Calculate the total weight of fish caught
    total_weight = 8 + 6*2 + 2*12  # 8-pound trout, 6 2-pound bass, 2 12-pound salmon

    # Calculate the number of campers that can be fed
    num_campers = total_weight // 2  # each camper eats 2 pounds of fish
    result = num_campers
    return result

print(solution())