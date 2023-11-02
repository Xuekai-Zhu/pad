def solution():
    # Calculate the number of girls in Camp Cedar
    num_girls = 40 * 3

    # Calculate the total number of children at Camp Cedar
    total_children = num_girls + 40

    # Calculate the number of counselors needed
    num_counselors = total_children // 8

    result = num_counselors
    return result

print(solution())