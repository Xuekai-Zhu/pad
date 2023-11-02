def solution():
    was_Godzilla_present = False
    is_Godzilla_immune_to_radiation = True
    if was_Godzilla_present and not is_Godzilla_immune_to_radiation:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())