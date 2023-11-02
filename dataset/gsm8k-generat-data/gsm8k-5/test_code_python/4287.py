def solution():
    total_plates = 20  # 8 plates with whole sprigs + 12 plates with 1/2 sprigs = 20 total plates decorated with parsley
    parsley_used = 8 + (12*0.5)  # The total amount of parsley used
    parsley_left = 25 - parsley_used  # The amount of parsley left
    result = parsley_left
    return result

print(solution())