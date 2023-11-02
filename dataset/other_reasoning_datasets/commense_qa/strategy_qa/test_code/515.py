def solution():
    creator = "Dick Wolf"
    emmy_years = [2007, 1997]
    statue_description = "winged woman holding an atom"
    if statue_description in creator + "'s home" and len(emmy_years) > 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())