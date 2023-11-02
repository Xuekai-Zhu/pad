def solution():
    """On a four-day trip, Carrie drove 135 miles the first day, 124 miles more the second day, 159 miles the third day, and 189 miles the fourth day. If she had to charge her phone every 106 miles, how many times did she charge her phone for the whole trip?"""
    # Calculate the total distance Carrie drove
    total_distance = 135 + 135 + 124 + 159 + 189

    # Calculate the number of times she charged her phone
    num_charges = total_distance // 106

    # Display the number of times she charged her phone
    result = num_charges
    return result

print(solution())