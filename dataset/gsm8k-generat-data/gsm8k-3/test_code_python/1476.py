def solution():
    """A small, old, wooden bridge can hold up to 100 kilograms at once. Mike, Megan, and Kelly are three children who decided to cross the bridge at the same time. Kelly weighs 34 kilograms, which is 15% less than Megan. Mike weighs 5 kilograms more than Megan. How much too much do the three children weigh together to cross the bridge?"""
    # Define the weight limit of the bridge
    BRIDGE_WEIGHT_LIMIT = 100

    # Calculate Megan's weight
    kelly_weight = 34
    megan_weight = kelly_weight * 1.15
    mike_weight = megan_weight + 5

    # Calculate the total weight of the three children
    total_weight = kelly_weight + megan_weight + mike_weight

    # Calculate how much too much weight there is
    too_much_weight = total_weight - BRIDGE_WEIGHT_LIMIT

    # Display how much too much weight there is
    result = too_much_weight
    return result

print(solution())