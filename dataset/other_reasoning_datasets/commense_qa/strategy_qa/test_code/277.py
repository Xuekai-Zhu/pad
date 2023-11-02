def solution():
    # Define that the Green Party of England Wales isn't registered in the USA and that people who live in England can't vote in the US
    GP_not_registered_USA = True
    England_residents_cant_vote_USA = True
    # Check if members of the Green Party of England and Wales can vote in the US
    if GP_not_registered_USA and not England_residents_cant_vote_USA:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())