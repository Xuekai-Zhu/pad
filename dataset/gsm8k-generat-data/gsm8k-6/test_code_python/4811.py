def solution():
    # Find the number of people with non-green eye colors
    non_green = 19 + (1/2)*100 + (1/4)*100  # 19 have blue eyes, half have brown eyes, and a quarter have black eyes

    # Find the number of people with green eyes
    green = 100 - non_green
    result = green
    return result

print(solution())