def solution():
    # Define what a Trek 9000 is and what an anchor is used for
    trek_9000 = "mountain bike"
    anchor = "used on water borne vehicles like boats"
    # Check if a Trek 9000 requires an anchor to park
    if trek_9000 != anchor:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())