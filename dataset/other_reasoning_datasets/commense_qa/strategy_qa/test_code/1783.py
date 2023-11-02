def solution():
    civil_war_start_year = 1861
    civil_war_end_year = 1865
    alaska_became_state_year = 1867
    northern_army_states = ["Maine", "New Hampshire", "Vermont", "Massachusetts", "Connecticut", "Rhode Island", "New York", "New Jersey", "Pennsylvania", "Ohio", "Indiana", "Illinois", "Michigan", "Wisconsin", "Minnesota", "Iowa"]
    if alaska_became_state_year < civil_war_end_year:
        result = "no"
    else:
        result = "Alaska was not part of the Northern Army during the Civil War because it was not yet part of the United States."
    return result

print(solution())