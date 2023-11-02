def solution():
    """John's car gets 30 mpg.  He drives 20 miles to work each way 5 days a week.  He also drives another 40 miles a week for leisure travel. How many gallons of gas does he use a week?"""
    # Calculate the total number of miles John drives in a week
    work_miles = 20 * 2 * 5 # round trip to work, 5 days a week
    leisure_miles = 40
    total_miles = work_miles + leisure_miles

    # Calculate the total gallons of gas John uses in a week
    mpg = 30
    gallons_per_mile = 1 / mpg
    total_gallons = total_miles * gallons_per_mile

    # Display the total gallons of gas
    result = total_gallons
    return result

print(solution())