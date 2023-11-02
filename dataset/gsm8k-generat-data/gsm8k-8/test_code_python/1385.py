def solution():
    # Calculate the length of the fence Cole has to pay for
    fence_length = (9 * 2) + (18 / 2)  # 36 feet

    # Calculate the portion of the fence the neighbor behind Cole will pay for
    neighbor1_contribution = fence_length / 2

    # Calculate the portion of the fence the neighbor on Cole's left will pay for
    neighbor2_contribution = (9 / 3) / 2  # 1.5 feet

    # Calculate the remaining length of fence Cole has to pay for
    remaining_fencelength = fence_length - neighbor1_contribution - neighbor2_contribution

    # Calculate the total cost of the fence for Cole
    fence_cost = remaining_fencelength * 3  # $108

    result = fence_cost
    return result

print(solution())