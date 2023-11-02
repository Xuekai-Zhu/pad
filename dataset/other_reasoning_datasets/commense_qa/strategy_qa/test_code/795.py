def solution():
    # Define the qualifications of full time and adjunct professors at SUNY schools
    full_time_requirement = "doctorate"
    adjunct_requirement = "masters"
    # Check if a doctorate is required to teach at a SUNY school
    if full_time_requirement == "doctorate":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())