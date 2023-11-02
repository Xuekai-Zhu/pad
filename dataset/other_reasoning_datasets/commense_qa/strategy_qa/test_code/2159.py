def solution():
    # Define fields of study
    astronomy_field = "celestial bodies"
    biology_field = "Drosophila"
    # Check if an astronomer is interested in Drosophila
    if astronomy_field != biology_field:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())