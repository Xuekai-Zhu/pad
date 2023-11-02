def solution():
    sammy_slices = 15
    tammy_slices = 2 * sammy_slices
    ron_slices = int(tammy_slices * 0.8)  # Ron eats 20% fewer pickles slices than Tammy
    result = ron_slices
    return result

print(solution())