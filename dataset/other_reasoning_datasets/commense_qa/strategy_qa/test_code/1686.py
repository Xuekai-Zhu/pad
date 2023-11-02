def solution():
    george_bush_grew_up_in = "Texas"
    primary_language_in_texas = "English"
    primary_language_in_certain_parts_of_china = "Cantonese"
    if primary_language_in_texas != primary_language_in_certain_parts_of_china and george_bush_grew_up_in != primary_language_in_certain_parts_of_china:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())