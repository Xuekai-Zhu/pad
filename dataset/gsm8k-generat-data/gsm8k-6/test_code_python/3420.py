def solution():
    # Calculate the total value of the collection
    total_value = 4 * 15 + 20  # 4 figures worth $15 each, 1 worth $20
    # Calculate the total earning by selling each figure for $5 less
    total_earning = 5 * (4 * 15 + 20)  # 4 figures sold for $10 each, 1 figure sold for $15
    result = total_earning
    return result

print(solution())