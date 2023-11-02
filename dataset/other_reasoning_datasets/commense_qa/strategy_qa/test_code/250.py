def solution():
    # List the three examples of radioactive waste in popular media
    popular_media = ["Teenage Mutant Ninja Turtles", "Family Guy", "Daredevil"]
    # Check if there are more than one examples of radioactive waste in popular media
    if len(popular_media) > 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())