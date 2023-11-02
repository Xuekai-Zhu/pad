def solution():
    weight_per_plate = 30  # weight of each weight plate
    total_weight = weight_per_plate * 10  # total weight of all the weight plates
    increased_weight = total_weight * 0.2  # weight increase due to special technology
    final_weight = total_weight + increased_weight  # weight felt when being lowered
    result = final_weight
    return result

print(solution())