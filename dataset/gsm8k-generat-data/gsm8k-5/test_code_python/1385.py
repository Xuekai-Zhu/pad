def solution():
    # Calculate the total length of the fence needed
    total_length = 2 * 9 + 18  # two sides are 9 feet and the back is 18 feet

    # Calculate the length of the shared side with the neighbor behind
    shared_side = 9  # Since Cole needs to fence on three sides, the shared side is one of the 9-foot sides

    # Calculate the length of the shared side with the neighbor on the left
    shared_side_left = 9 / 3  # The neighbor on the left agreed to pay for one-third of the shared side

    # Calculate the total length of the shared sides
    total_shared_length = shared_side + shared_side_left

    # Calculate the length that Cole needs to pay for
    cole_length = total_length - total_shared_length

    # Calculate the cost of the fence
    fence_cost = cole_length * 3  # $3 per foot

    result = fence_cost
    return result

print(solution())