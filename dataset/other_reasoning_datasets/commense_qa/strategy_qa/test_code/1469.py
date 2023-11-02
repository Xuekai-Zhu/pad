def solution():
    is_solo_performed_by_single_musician = True
    is_department_of_defense_related_to_music = False
    if is_solo_performed_by_single_musician and not is_department_of_defense_related_to_music:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())