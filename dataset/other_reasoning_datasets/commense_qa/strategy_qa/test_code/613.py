def solution():
    # Define the characteristics of rosemary and lavender
    rosemary_scent = "pine-like"
    lavender_scent = "floral"
    # Check if scent is the easiest way to differentiate between the two
    if rosemary_scent != lavender_scent:
        result = "no, scent is the easiest way"
    else:
        result = "yes, looks are the easiest way"
    return result

print(solution())