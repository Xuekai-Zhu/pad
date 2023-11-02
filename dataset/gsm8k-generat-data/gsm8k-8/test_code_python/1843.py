def solution():
    darlene_mpg = 20
    martha_mpg = 0.5 * darlene_mpg
    miles_to_travel = 300

    # Calculate the gallons required for Martha's car
    gallons_required = miles_to_travel / martha_mpg
    result = gallons_required
    return result

print(solution())