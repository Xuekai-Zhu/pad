def solution():
    """Cole wants to fence his backyard on three sides. His backyard is 9 feet along the sides and 18 feet along the back. The neighbor behind him agreed to pay for half of their shared side of his fence, and the neighbor on his left agreed to pay for a third of their shared side. Fencing costs $3 per foot. How much does Cole have to pay for the fence?"""
    side_length = 9
    back_length = 18
    total_length = (2 * side_length) + back_length
    shared_side_cost = (total_length/2) * 3
    shared_left_side_cost = (side_length/3) * 3
    cole_cost = (total_length - (side_length/2) - (side_length/3)) * 3
    total_cost = cole_cost + shared_side_cost + shared_left_side_cost
    result = total_cost
    return result

print(solution())