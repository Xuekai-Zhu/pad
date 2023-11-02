def solution():
    # Calculate the number of people who didn't show up
    no_show = 0.2 * 30

    # Calculate the number of people who showed up
    show_up = 30 - no_show

    # Calculate the number of people who ordered steak
    steak = 0.75 * show_up

    # Calculate the number of people who ordered chicken
    chicken = show_up - steak

    result = chicken
    return result

print(solution())