def solution():
    total_days = 120  # It takes 120 days for a butterfly egg to become a butterfly
    larva_time = total_days / 4  # Each butterfly spends 3 times as much time as a larva as in a cocoon
    cocoon_time = larva_time / 3  # Each butterfly spends 1/3 of its time in a cocoon

    result = cocoon_time
    return result

print(solution())