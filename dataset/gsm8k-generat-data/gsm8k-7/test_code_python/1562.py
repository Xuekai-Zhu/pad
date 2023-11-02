def solution():
    num_blocks = 3
    candies_per_block = 30
    candies_per_necklace = 10
    
    # Calculate total number of candies available
    total_candies = num_blocks * candies_per_block
    
    # Calculate number of candy necklaces that can be made
    num_necklaces = total_candies // candies_per_necklace
    
    # Each friend receives one necklace, so the number of friends is equal to the number of necklaces
    num_friends = num_necklaces
    
    result = num_friends
    return result

print(solution())