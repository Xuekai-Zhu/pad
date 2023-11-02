def solution():
    """Cole wants to fence his backyard on three sides. His backyard is 9 feet along the sides and 18 feet along the back. The neighbor behind him agreed to pay for half of their shared side of his fence, and the neighbor on his left agreed to pay for a third of their shared side. Fencing costs $3 per foot. How much does Cole have to pay for the fence?"""
    # Define the length of each side of Cole's backyard
    side_length = 9
    back_length = 18

    # Calculate the total length of fencing needed
    total_length = (2 * side_length) + back_length

    # Calculate the length of fencing the neighbor behind will pay for
    neighbor_behind_length = back_length / 2

    # Calculate the length of fencing the neighbor on the left will pay for
    neighbor_left_length = side_length / 3

    # Calculate the length of fencing Cole will have to pay for
    cole_length = total_length - neighbor_behind_length - neighbor_left_length

    # Calculate the total cost of the fence
    total_cost = cole_length * 3

    # Display the cost Cole has to pay
    result = total_cost
    return result

print(solution())