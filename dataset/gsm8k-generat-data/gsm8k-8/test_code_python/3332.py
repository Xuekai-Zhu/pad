def solution():
    # Define the ratio of Nancy's stepping to Jason's stepping
    nancy_to_jason_ratio = 3/1
    
    # Calculate the total number of times Nancy steps on her partner's feet
    nancy_total = 3 * nancy_to_jason_ratio
    
    # Calculate the total number of times Jason steps on his partner's feet
    jason_total = (32 - nancy_total) / 4
    
    result = jason_total
    return result

print(solution())