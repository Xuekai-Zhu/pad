def solution():
    # Calculate the total number of miles Marcus traveled during the road trip
    total_miles = 2 * 20 * 30  # Marcus filled his gas tank twice and his car gets 30 miles per gallon and holds 20 gallons of gas
    # Calculate the number of miles Marcus' car has on it now
    miles_now = 1728 + total_miles
    result = miles_now
    return result

print(solution())