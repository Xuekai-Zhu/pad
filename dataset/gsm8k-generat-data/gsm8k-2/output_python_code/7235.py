def solution():
    """The school has 14 boys and 10 girls. If 4 boys and 3 girls drop out, how many boys and girls are left?"""
    total_boys = 14
    total_girls = 10
    dropped_boys = 4
    dropped_girls = 3
    remaining_boys = total_boys - dropped_boys
    remaining_girls = total_girls - dropped_girls
    result = (remaining_boys, remaining_girls)
    return result

print(solution())