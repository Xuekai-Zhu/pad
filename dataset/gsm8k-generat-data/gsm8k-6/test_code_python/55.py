def solution():
    # Calculate the total number of flowers
    total_flowers = 25 + 40 + 35

    # Calculate the number of flowers that are not roses
    non_roses = total_flowers - 25

    # Calculate the percentage of flowers that are not roses
    percentage = (non_roses / total_flowers) * 100
    result = percentage
    return result

print(solution())