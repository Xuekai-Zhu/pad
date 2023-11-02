def solution():
    cone_scoops = 1  # number of scoops in a cone
    banana_split_scoops = 3 * cone_scoops  # number of scoops in a banana split
    waffle_bowl_scoops = banana_split_scoops + 1  # number of scoops in a waffle bowl
    total_scoops = cone_scoops + banana_split_scoops + waffle_bowl_scoops + (2 * cone_scoops)  # total number of scoops
    result = total_scoops
    return result

print(solution())