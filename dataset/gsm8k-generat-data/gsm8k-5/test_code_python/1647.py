def solution():
    # Calculate the number of times Sarah saw her reflection
    tall_mirror_sarah = 10 * 3 * 5  # 10 reflections per visit, 3 visits, 5 times passing through
    wide_mirror_sarah = 5 * 5 * 2  # 5 reflections per visit, 5 visits, 2 times passing through
    total_sarah = tall_mirror_sarah + wide_mirror_sarah

    # Calculate the number of times Ellie saw her reflection
    tall_mirror_ellie = 6 * 3 * 5  # 6 reflections per visit, 3 visits, 5 times passing through
    wide_mirror_ellie = 3 * 5 * 2  # 3 reflections per visit, 5 visits, 2 times passing through
    total_ellie = tall_mirror_ellie + wide_mirror_ellie

    # Calculate the total number of times they saw their reflections
    total_reflections = total_sarah + total_ellie
    result = total_reflections
    return result

print(solution())