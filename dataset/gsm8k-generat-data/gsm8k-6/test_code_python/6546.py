def solution():
    # Calculate the number of people who didn't show up
    no_show = 0.20 * 30

    # Calculate the number of people who showed up
    showed_up = 30 - no_show

    # Calculate the number of people who ordered steak
    steak_people = 0.75 * showed_up

    # Calculate the number of people who ordered chicken
    chicken_people = showed_up - steak_people

    result = chicken_people
    return result

print(solution())