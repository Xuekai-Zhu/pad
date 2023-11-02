def solution():
    # Define that Antarctica has no permanent residents and that exposure to the elements could be deadly
    antarctica_permanent_residents = False
    elements_deadly = True
    # Check if there are problems relating to homelessness in Antarctica
    if antarctica_permanent_residents and elements_deadly:
        result = "no"
    else:
        result = "not applicable"
    return result

print(solution())