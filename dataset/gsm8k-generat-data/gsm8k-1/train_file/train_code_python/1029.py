def solution():
    """While preparing for a meeting, Bill fills Dixie cups with water from out of a water cooler. The water cooler initially contains 3 gallons of water, and each Dixie cup holds 6 ounces of water. If Bill fills one cup of water per each meeting chair, and there are 5 rows of meeting chairs with 10 chairs in each row, then how many ounces of water will be left in the cooler after all cups have been are filled? (There are 128 ounces in a gallon.)"""
    gallons_initial = 3
    ounces_per_gallon = 128
    cups_per_chair = 1
    rows = 5
    chairs_per_row = 10
    total_chairs = rows * chairs_per_row
    total_cups = total_chairs * cups_per_chair
    ounces_per_cup = 6
    total_ounces = total_cups * ounces_per_cup
    ounces_left = (gallons_initial * ounces_per_gallon) - total_ounces
    result = ounces_left
    return result

print(solution())