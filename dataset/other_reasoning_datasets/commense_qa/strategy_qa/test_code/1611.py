def solution():
    gomer_pyle_in_usmc = True
    lieutenant_rank = "Lieutenant"
    # Check if Gomer Pyle would be required to salute a lieutenant
    if gomer_pyle_in_usmc and lieutenant_rank in ["Lieutenant", "First Lieutenant", "Second Lieutenant"]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())