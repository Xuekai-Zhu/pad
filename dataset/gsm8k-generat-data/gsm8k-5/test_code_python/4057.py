def solution():
    violets_nails = 27  # Violet has 27 nails
    ttoes_nails = (violets_nails - 3) / 2  # Tickletoe has 3 less and half as many nails as Violet
    total_nails = violets_nails + ttoes_nails  # Calculate the total number of nails

    result = total_nails
    return result

print(solution())