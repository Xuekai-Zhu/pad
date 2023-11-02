def solution():
    founders = ["Ben Cohen", "Jerry Greenfield"]
    still_involved = False
    # Check if both founders are still involved in the company
    if "Ben Cohen" in founders and "Jerry Greenfield" in founders:
        still_involved = True
    if still_involved:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())