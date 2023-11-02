def solution():
    total_bollards = 4000
    bollards_installed = total_bollards * 3/4
    bollards_remaining = total_bollards - bollards_installed
    result = bollards_remaining
    return result

print(solution())