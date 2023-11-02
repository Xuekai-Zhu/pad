def solution():
    maggie_share = 4500
    debby_share_percent = 0.25  # 25%
    
    # Calculate the total amount of money shared
    total_share = maggie_share / (1 - debby_share_percent)

    result = total_share
    return result

print(solution())