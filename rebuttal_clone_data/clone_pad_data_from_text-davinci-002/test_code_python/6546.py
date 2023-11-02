def solution():
    num_invited = 30
    num_no_show = num_invited * .2
    num_attendees = num_invited - num_no_show
    steak_eaters = num_attendees * .75
    chicken_eaters = num_attendees - steak_eaters
    result = chicken_eaters
    return result

print(solution())