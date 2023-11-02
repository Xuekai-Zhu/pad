def solution():
    """The school has 14 boys and 10 girls. If 4 boys and 3 girls drop out, how many boys and girls are left?"""
    initial_boys = 14
    initial_girls = 10
    boys_drop_out = 4
    girls_drop_out = 3
    boys_left = initial_boys - boys_drop_out
    girls_left = initial_girls - girls_drop_out
    result = (boys_left, girls_left)
    return result

print(solution())