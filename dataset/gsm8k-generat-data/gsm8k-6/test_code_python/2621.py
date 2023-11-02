def solution():
    # Calculate the number of blue hangers
    blue_hangers = 4 - 1  # one less blue hanger than there are green hangers

    # Calculate the number of yellow hangers
    yellow_hangers = blue_hangers - 1  # one less yellow hanger than there are blue hangers

    # Calculate the total number of colored hangers
    total_hangers = 7 + 4 + blue_hangers + yellow_hangers  # 7 pink hangers, 4 green hangers, blue and yellow hangers as calculated above
    result = total_hangers
    return result

print(solution())