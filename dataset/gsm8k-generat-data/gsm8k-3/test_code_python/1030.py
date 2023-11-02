def solution():
    """While preparing for a meeting, Bill fills Dixie cups with water from out of a water cooler. The water cooler initially contains 3 gallons of water, and each Dixie cup holds 6 ounces of water.  If Bill fills one cup of water per each meeting chair, and there are 5 rows of meeting chairs with 10 chairs in each row, then how many ounces of water will be left in the cooler after all cups have been are filled? (There are 128 ounces in a gallon.)"""
    # Define the initial amount of water in the cooler in ounces
    water_in_gallons = 3
    water_in_ounces = water_in_gallons * 128

    # Calculate the number of Dixie cups needed
    num_cups = 5 * 10

    # Calculate the amount of water used in filling the Dixie cups
    water_used = num_cups * 6

    # Calculate the amount of water left in the cooler
    water_left = water_in_ounces - water_used

    # Display the amount of water left in the cooler
    result = water_left
    return result

print(solution())