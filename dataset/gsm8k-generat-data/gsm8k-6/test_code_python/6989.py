def solution():
    # Calculate the number of paintings the artist can complete in 1 week
    paintings_per_week = 30 // 3  # it takes 3 hours to complete a painting
    
    # Calculate the total number of paintings the artist can complete in 4 weeks
    total_paintings = paintings_per_week * 4
    
    result = total_paintings
    return result

print(solution())