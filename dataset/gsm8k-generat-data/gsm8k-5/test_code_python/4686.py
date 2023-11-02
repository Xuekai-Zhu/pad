def solution():
    total_shirts = 20
    total_shorts = 8
    folded_shirts = 12
    folded_shorts = 5

    # Calculate the remaining pieces of clothing to fold
    remaining_shirts = total_shirts - folded_shirts
    remaining_shorts = total_shorts - folded_shorts
    total_remaining = remaining_shirts + remaining_shorts
    
    result = total_remaining
    return result

print(solution())