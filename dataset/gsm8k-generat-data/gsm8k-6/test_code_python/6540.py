def solution():
    # Find Annie's and Tom's toy numbers using Mike's toy number
    mike_toys = 6
    annie_toys = 3 * mike_toys
    tom_toys = annie_toys + 2

    # Find the total number of toys
    total_toys = mike_toys + annie_toys + tom_toys
    result = total_toys
    return result

print(solution())