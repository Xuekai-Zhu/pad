def solution():
    # Calculate the total number of berets James can make
    total_berets = min(12//3, 15//3, 6//3)  # Round down the number of berets he can make from each color and find the minimum
    result = total_berets
    return result

print(solution())