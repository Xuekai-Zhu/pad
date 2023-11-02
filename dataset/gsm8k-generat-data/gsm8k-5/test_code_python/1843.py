def solution():
    darlene_mpg = 20  # Darlene's car gets 20 miles/gallon
    martha_mpg = darlene_mpg / 2  # Martha's car gets half as many miles per gallon as Darlene's car
    distance = 300  # The trip is 300 miles long

    # Calculate how many gallons Martha's car requires
    gallons_required = distance / martha_mpg
    result = gallons_required
    return result

print(solution())