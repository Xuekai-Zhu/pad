def solution():
    # Calculate the total number of treats Tim's children get while trick or treating
    treats_per_hour = 5 * 3  # 5 houses visited per hour, each house gives 3 treats per kid
    total_treats = treats_per_hour * 3 * 4  # 3 children, out for 4 hours
    result = total_treats
    return result

print(solution())