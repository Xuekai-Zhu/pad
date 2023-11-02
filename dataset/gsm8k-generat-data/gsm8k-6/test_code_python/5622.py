def solution():
    # Calculate how much weight Michael has already lost
    already_lost = 3 + 4
    
    # Calculate how much weight Michael has left to lose
    left_to_lose = 10 - already_lost
    
    # Calculate how much weight Michael needs to lose in May
    weight_to_lose_in_May = left_to_lose / 2  # Assuming May is halfway between March and June
    
    result = weight_to_lose_in_May
    return result

print(solution())