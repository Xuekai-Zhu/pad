def solution():
    total_toys = 24  # There are 24 toys in the box
    action_figures = total_toys * (1/4)  # 1/4 of the toys are action figures
    dolls = total_toys - action_figures  # The remaining toys are all dolls
    result = dolls
    return result

print(solution())