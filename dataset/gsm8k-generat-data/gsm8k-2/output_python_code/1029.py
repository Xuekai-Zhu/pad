def solution():
    """While preparing for a meeting, Bill fills Dixie cups with water from out of a water cooler. The water cooler initially contains 3 gallons of water, and each Dixie cup holds 6 ounces of water. If Bill fills one cup of water per each meeting chair, and there are 5 rows of meeting chairs with 10 chairs in each row, then how many ounces of water will be left in the cooler after all cups have been are filled? (There are 128 ounces in a gallon.)"""
    water_cooler_size = 3 * 128
    num_chairs = 5 * 10
    water_per_cup = 6
    total_water_needed = num_chairs * water_per_cup
    water_left = water_cooler_size - total_water_needed
    result = water_left
    return result

print(solution())