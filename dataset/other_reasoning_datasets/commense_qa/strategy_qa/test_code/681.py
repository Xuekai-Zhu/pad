def solution():
    homeopathy_doctors = True
    internal_medicine_doctors = False
    if homeopathy_doctors and not internal_medicine_doctors:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())