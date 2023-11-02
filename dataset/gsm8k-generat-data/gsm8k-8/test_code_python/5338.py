def solution():
    # Calculate the number of dress shirts ironed
    dress_shirts_irons = 4 * 3 # Rick can iron 4 dress shirts in 1 hour, so in 3 hours he can iron 4 x 3 = 12 dress shirts

    # Calculate the number of dress pants ironed
    dress_pants_irons = 3 * 5 # Rick can iron 3 dress pants in 1 hour, so in 5 hours he can iron 3 x 5 = 15 dress pants

    # Calculate the total number of clothing pieces ironed
    total_irons = dress_shirts_irons + dress_pants_irons
    result = total_irons
    return result

print(solution())