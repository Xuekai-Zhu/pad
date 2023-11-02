def solution():
    # Define the number of scoops in each order
    cone_scoops = 1
    banana_scoops = 3 * cone_scoops
    waffle_scoops = banana_scoops + 1

    # Calculate the total number of scoops
    total_scoops = cone_scoops + banana_scoops + waffle_scoops + (2 * cone_scoops)

    result = total_scoops
    return result

print(solution())