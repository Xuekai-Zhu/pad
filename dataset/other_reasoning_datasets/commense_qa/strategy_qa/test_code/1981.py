def solution():
    attended_secondary_education = True
    pursued_higher_education = False
    if attended_secondary_education and not pursued_higher_education:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())