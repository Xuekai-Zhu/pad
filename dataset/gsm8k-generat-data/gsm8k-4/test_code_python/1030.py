def solution():
    """While preparing for a meeting, Bill fills Dixie cups with water from out of a water cooler. The water cooler initially contains 3 gallons of water, and each Dixie cup holds 6 ounces of water. If Bill fills one cup of water per each meeting chair, and there are 5 rows of meeting chairs with 10 chairs in each row, then how many ounces of water will be left in the cooler after all cups have been are filled? (There are 128 ounces in a gallon.)"""
    # Define the initial amount of water in the cooler and the amount of water in one cup
    initial_water = 3 * 128
    cup_water = 6

    # Calculate the total number of cups to be filled
    total_cups = 5 * 10

    # Calculate the total amount of water used to fill all the cups
    total_water_used = total_cups * cup_water

    # Calculate the amount of water left in the cooler
    water_left = initial_water - total_water_used

    # Return the result in ounces
    result = water_left
    return result

print(solution())