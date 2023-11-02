def solution():
    cone_scoops = 1
    son_cone_scoops = 2
    daughter_cone_scoops = 1
    banana_split_scoops = 3 * cone_scoops
    waffle_bowl_scoops = banana_split_scoops + 1

    # Calculate the total number of scoops of ice cream served
    total_scoops = cone_scoops + son_cone_scoops + daughter_cone_scoops + banana_split_scoops + waffle_bowl_scoops
    result = total_scoops
    return result

print(solution())