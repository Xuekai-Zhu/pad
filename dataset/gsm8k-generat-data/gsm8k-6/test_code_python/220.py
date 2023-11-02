def solution():
    # Calculate the gallons of gas needed to travel 600 miles round trip
    gallons_per_mile = 20 / 400  # car uses 20 gallons to travel 400 miles
    total_gallons_needed = 2 * 600 * gallons_per_mile  # round trip of 600 miles
    additional_gallons_needed = total_gallons_needed - 8  # Mr. Montero's car has 8 gallons in it

    result = additional_gallons_needed
    return result

print(solution())