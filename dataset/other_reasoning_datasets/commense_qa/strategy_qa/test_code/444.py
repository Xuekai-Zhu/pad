def solution():
    # Compare the hearing abilities of grey seals and dogs
    grey_seals_hearing = "better underwater"
    dogs_hearing = "can hear from far away"
    if dogs_hearing > grey_seals_hearing:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())