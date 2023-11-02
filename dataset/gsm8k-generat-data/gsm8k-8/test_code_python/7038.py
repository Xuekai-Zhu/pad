def solution():
    # Define the initial number of puppies and kittens
    puppies = 7
    kittens = 6
    
    # Subtract the number of pets sold
    puppies -= 2
    kittens -= 3
    
    # Calculate the total number of pets remaining
    total_remaining = puppies + kittens
    
    result = total_remaining
    return result

print(solution())