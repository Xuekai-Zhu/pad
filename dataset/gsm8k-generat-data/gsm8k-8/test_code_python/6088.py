def solution():
    # Convert 4 dozen to total number of shirts
    total_shirts = 4 * 12

    # Calculate the number of shirts Kim's sister takes
    sister_shirts = total_shirts * (1/3)

    # Calculate the number of shirts Kim has left
    shirts_left = total_shirts - sister_shirts
    result = shirts_left
    return result

print(solution())