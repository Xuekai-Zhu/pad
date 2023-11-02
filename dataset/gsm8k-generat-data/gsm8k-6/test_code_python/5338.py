def solution():
    # Calculate the total number of dress shirts ironed by Rick
    dress_shirts = 4 * 3  # Rick can iron 4 dress shirts in an hour and he spends 3 hours ironing dress shirts
    # Calculate the total number of dress pants ironed by Rick
    dress_pants = 3 * 5  # Rick can iron 3 dress pants in an hour and he spends 5 hours ironing dress pants
    # Calculate the total number of pieces of clothing ironed by Rick
    total_clothing = dress_shirts + dress_pants
    result = total_clothing
    return result

print(solution())