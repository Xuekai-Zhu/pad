def solution():
    # Calculate the number of people who didn't show up
    did_not_show_up = 0.2 * 30

    # Calculate the number of people who showed up
    showed_up = 30 - did_not_show_up

    # Calculate the number of people who ordered steak
    steak_ordered = 0.75 * showed_up

    # Calculate the number of people who ordered chicken
    chicken_ordered = showed_up - steak_ordered
    result = chicken_ordered
    return result

print(solution())