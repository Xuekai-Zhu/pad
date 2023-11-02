def solution():
    DIY_hem_method = "adhesive"
    professional_hem_method = "needle and thread"
    expensive_tailor = True
    if expensive_tailor:
        result = "no"
    else:
        if DIY_hem_method == "adhesive":
            result = "yes"
        elif professional_hem_method == "needle and thread":
            result = "no"
    return result

print(solution())