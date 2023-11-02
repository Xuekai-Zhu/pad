def solution():
    # Define the total fruit consumed in ounces
    total_fruit_oz = 8 * 16

    # Subtract the ounces of oranges and apples to find out the ounces of peaches
    peach_oz = total_fruit_oz - 8 * 1 - 24

    # Convert the ounces of peaches to pounds
    peach_lbs = peach_oz / 16
    result = peach_lbs
    return result

print(solution())