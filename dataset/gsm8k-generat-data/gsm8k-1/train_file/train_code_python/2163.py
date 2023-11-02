def solution():
    """There are 24 toys in the box and ¼ of them are action figures. The remaining toys are all dolls. How many dolls are there?"""
    total_toys = 24
    action_figures = total_toys / 4
    dolls = total_toys - action_figures
    result = dolls
    return result

print(solution())