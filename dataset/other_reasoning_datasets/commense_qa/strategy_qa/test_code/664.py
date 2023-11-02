def solution():
    age_of_quadragenarians = "40s"
    percentage_of_memory_loss_over_50 = 50
    ken_jennings_age_when_winning = 46
    if age_of_quadragenarians == "40s":
        result = "It cannot be determined with the given information."
    else:
        result = "no"
        if ken_jennings_age_when_winning > 50:
            result = "yes"
    return result

print(solution())