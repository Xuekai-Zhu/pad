def solution():
    # Find the number of lollipops that Marlon gave to Emily
    lollipops_to_Emily = (2/3) * 42  

    # Find the number of lollipops that Marlon kept
    lollipops_kept = 4

    # Find the number of lollipops that Marlon gave to Lou
    lollipops_to_Lou = 42 - lollipops_to_Emily - lollipops_kept

    result = lollipops_to_Lou
    return result

print(solution())