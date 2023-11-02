def solution():
    supreme_court_appointments = "appointed"
    simon_cowell_voting_rights = "British"
    if supreme_court_appointments == "appointed" and simon_cowell_voting_rights != "American":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())