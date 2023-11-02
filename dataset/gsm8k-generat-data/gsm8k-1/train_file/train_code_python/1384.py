def solution():
    """Cole wants to fence his backyard on three sides. His backyard is 9 feet along the sides and 18 feet along the back. The neighbor behind him agreed to pay for half of their shared side of his fence, and the neighbor on his left agreed to pay for a third of their shared side. Fencing costs $3 per foot. How much does Cole have to pay for the fence?"""
    
    side_length = 9
    back_length = 18
    shared_side_length = side_length/2
    
    # Calculating the length of the sides Cole has to pay for
    left_side_length = side_length - (shared_side_length/3)
    right_side_length = side_length - shared_side_length
    
    # Calculating the total length of fence needed
    total_fence_length = 2*side_length + back_length
    
    # Calculating the cost of fence
    total_cost = (total_fence_length-shared_side_length/2)*3
    
    # Subtracting the amount paid by neighbors for shared side length
    total_cost -= (shared_side_length/2)*3/2
    total_cost -= (shared_side_length/3)*3
    
    result = total_cost
    
    return result

print(solution())