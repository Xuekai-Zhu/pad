def solution():
    # Define the number of trash cans added to the streets
    street_cans = 14
    
    # Define the number of trash cans added to the back of stores
    store_cans = 2 * street_cans
    
    # Calculate the total number of trash cans
    total_cans = street_cans + store_cans
    
    result = total_cans
    return result

print(solution())