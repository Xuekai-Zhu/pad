def solution():
    total_deer = 920  # There are 920 deer in the park
    eight_antler_deer = total_deer * 0.1  # 10% of the deer have 8 antlers
    albino_eight_antler_deer = eight_antler_deer * 0.25  # A quarter of the 8-antlered deer also have albino fur
    result = albino_eight_antler_deer
    return result

print(solution())