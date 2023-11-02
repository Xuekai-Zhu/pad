def solution():
    num_invited = 30
    percent_no_show = 0.2
    percent_steak = 0.75

    # Calculate the number of people who didn't show up
    num_no_show = num_invited * percent_no_show

    # Calculate the number of people who did show up
    num_show = num_invited - num_no_show

    # Calculate the number of people who ordered steak
    num_steak = num_show * percent_steak

    # Calculate the number of people who ordered chicken
    num_chicken = num_show - num_steak
    result = num_chicken
    return result

print(solution())