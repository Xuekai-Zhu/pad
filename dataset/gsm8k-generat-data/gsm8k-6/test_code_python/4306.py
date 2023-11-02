def solution():
    total_deer = 920
    eight_antlers = 0.1 * total_deer # 10% of the deer have 8 antlers
    albino_eight_antlers = 0.25 * eight_antlers # a quarter of the deer with 8 antlers have albino fur
    result = albino_eight_antlers
    return result

print(solution())