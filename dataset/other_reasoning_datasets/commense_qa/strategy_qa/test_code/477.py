def solution():
    anxious_person = True
    medication_or_therapy = True
    wizard_of_oz_giving_courage = False
    if anxious_person and medication_or_therapy and not wizard_of_oz_giving_courage:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())