def solution():
    parody_protected = "fair use"
    political_leader_criticism_protected = "1st Amendment"
    president_of_US = True
    # Check if parodies of the President are protected under fair use or 1st Amendment
    if parody_protected == "fair use" or political_leader_criticism_protected == "1st Amendment":
        result = "no, they are not illegal"
    else:
        result = "yes, they are illegal"
    return result

print(solution())