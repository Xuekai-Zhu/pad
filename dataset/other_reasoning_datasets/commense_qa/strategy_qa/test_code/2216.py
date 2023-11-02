def solution():
    gujarati_script_type = "abugida"
    kanji_script_type = "logographic"
    if gujarati_script_type == kanji_script_type:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())