def solution():
    field_of_study = "zoology"
    focus_areas = ["behavior", "classification", "science", "fossils"]
    relevant_mythology = "Romanian mythology"
    relevant_creatures = ["strigoi"]
    if (field_of_study == "zoology") and (set(focus_areas) & set([relevant_mythology] + relevant_creatures)):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())