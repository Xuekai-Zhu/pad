def solution():
    """Cole wants to fence his backyard on three sides. His backyard is 9 feet along the sides and 18 feet along the back. The neighbor behind him agreed to pay for half of their shared side of his fence, and the neighbor on his left agreed to pay for a third of their shared side. Fencing costs $3 per foot. How much does Cole have to pay for the fence?"""
    # Calculate the length of each side of Cole's backyard
    side_length = 9
    back_length = 18

    # Calculate the total length of the fence needed
    total_length = 2 * side_length + back_length

    # Calculate the portion of the shared side that Cole needs to pay for
    shared_side_length = back_length / 2
    neighbor_contribution = shared_side_length / 2 + shared_side_length / 3

    # Calculate the total cost of the fence
    total_cost = (total_length - shared_side_length) * 3 + neighbor_contribution * 3

    # return the result
    result = total_cost
    return result

print(solution())