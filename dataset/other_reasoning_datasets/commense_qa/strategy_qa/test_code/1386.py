def solution():
    school_name = "Gallaudet"
    primary_mode_of_communication = "sign language"
    is_loudspeaker_reliant = False
    # Check if a loudspeaker would be useful for most Gallaudet students
    if primary_mode_of_communication != "voice" and not is_loudspeaker_reliant:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())