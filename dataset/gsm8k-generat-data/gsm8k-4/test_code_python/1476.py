def solution():
    """A small, old, wooden bridge can hold up to 100 kilograms at once. Mike, Megan, and Kelly are three children who decided to cross the bridge at the same time. Kelly weighs 34 kilograms, which is 15% less than Megan. Mike weighs 5 kilograms more than Megan. How much too much do the three children weigh together to cross the bridge?"""
    # Define the maximum weight the bridge can hold
    MAX_WEIGHT = 100

    # Calculate the weight of Kelly
    kelly_weight = 34

    # Calculate the weight of Megan
    megan_weight = kelly_weight / 0.85

    # Calculate the weight of Mike
    mike_weight = megan_weight + 5

    # Calculate the total weight of the three children
    total_weight = kelly_weight + megan_weight + mike_weight

    # Calculate the excess weight
    excess_weight = total_weight - MAX_WEIGHT

    result = excess_weight
    return result

print(solution())