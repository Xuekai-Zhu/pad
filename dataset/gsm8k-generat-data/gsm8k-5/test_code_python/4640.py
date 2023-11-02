def solution():
    colored_pencils = 14  # Teresa has 14 colored pencils
    black_pencils = 35  # Teresa has 35 black pencils
    total_pencils = colored_pencils + black_pencils  # Total number of pencils Teresa has
    total_pencils -= 10  # Teresa keeps 10 pencils for herself
    num_siblings = 3  # Teresa has three siblings to share her pencils with

    # Calculate how many pencils each sibling gets, rounded down to a whole number
    pencils_per_sibling = total_pencils // num_siblings
    result = pencils_per_sibling
    return result

print(solution())