def solution():
    """Rick took off on a road trip for the summer. He traveled to the first destination on his trip, and then from there, he traveled twice the distance to this second destination. The third point on his trip was 40 miles away, which was half the distance he traveled from the beginning to his first destination. The final destination took twice the amount of driving of all the other legs put together. How many miles in total did he travel across all the legs of the trip?"""
    
    # First leg of the trip
    first_dest = x
    second_dest = 2 * first_dest
    
    # Second leg of the trip
    third_dest = 40
    first_to_second = first_dest + second_dest
    fourth_dest = 2 * (first_to_second + third_dest)
    
    # Total distance traveled
    total_dist = first_dest + second_dest + third_dest + fourth_dest
    
    return total_dist

print(solution())