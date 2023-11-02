def solution():
    # Calculate the number of scoops in each order
    cone_scoops = 1
    banana_split_scoops = 3 * cone_scoops
    waffle_bowl_scoops = banana_split_scoops + 1

    # Calculate the total number of scoops served
    total_scoops = cone_scoops + banana_split_scoops + waffle_bowl_scoops + 2 * cone_scoops

    result = total_scoops
    return result

print(solution())