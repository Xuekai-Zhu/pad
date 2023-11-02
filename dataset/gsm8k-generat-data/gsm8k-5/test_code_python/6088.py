def solution():
    shirts = 4 * 12  # Kim has 4 dozen (4*12) shirts
    sister_shirts = shirts / 3  # Kim's sister takes 1/3 of the shirts
    remaining_shirts = shirts - sister_shirts  # Kim has the remaining shirts

    result = remaining_shirts
    return result

print(solution())