def solution():
    iggy_pop_name = "James Newell Osterberg Jr."
    iggy_pop_father_name = "James Newell Osterberg Sr."
    if iggy_pop_name.startswith("James Newell") and iggy_pop_father_name == "James Newell Osterberg Sr.":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())