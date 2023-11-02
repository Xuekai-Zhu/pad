def solution():
    # Find the number of nails Tickletoe has
    violets_nails = 27
    t_nails = (violets_nails - 3) / 2

    # Calculate the total number of nails they have together
    total_nails = violets_nails + t_nails
    result = total_nails
    return result

print(solution())