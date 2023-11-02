def solution():
    # Define the burial places of Carl Linnaeus and Michael Jackson
    carl_linnaeus_resting_place = "Uppsala Cathedral"
    michael_jackson_resting_place = "Forest Lawn Memorial Park"
    # Check if they have the same final resting place
    if carl_linnaeus_resting_place == michael_jackson_resting_place:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())