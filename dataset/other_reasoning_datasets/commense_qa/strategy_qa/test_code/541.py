def solution():
    skull_form = "inwards"
    fission_lines_present = True
    if skull_form == "inwards" and fission_lines_present:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())