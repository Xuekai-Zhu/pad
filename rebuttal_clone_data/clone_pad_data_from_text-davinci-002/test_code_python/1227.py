def solution():
    total_crayons_francine = 85
    total_crayons_friend = 27
    total_crayons = total_crayons_francine + total_crayons_friend
    crayons_per_box = total_crayons / 5
    result = crayons_per_box - 5
    return result

print(solution())