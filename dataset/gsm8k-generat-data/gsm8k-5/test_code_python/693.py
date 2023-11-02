def solution():
    total_roses = 20  # Ian had 20 roses
    roses_given = 6 + 9 + 4  # Ian gave away 6+9+4 = 19 roses
    roses_kept = total_roses - roses_given  # The remaining roses were kept by Ian
    result = roses_kept
    return result

print(solution())