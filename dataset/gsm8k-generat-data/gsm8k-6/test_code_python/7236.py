def solution():
    # Find the number of boys remaining in the school
    boys_remaining = 14 - 4  # 4 boys dropped out

    # Find the number of girls remaining in the school
    girls_remaining = 10 - 3  # 3 girls dropped out

    # Return the number of remaining boys and girls as a tuple
    result = (boys_remaining, girls_remaining)
    return result

print(solution())