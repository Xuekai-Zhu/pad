def solution():
    # Calculate Megan's weight based on Kelly's weight
    kelly_weight = 34
    megan_weight = kelly_weight / 0.85  # Kelly's weight is 15% less than Megan's weight
    mike_weight = megan_weight + 5  # Mike weighs 5 kilograms more than Megan

    # Calculate the total weight of the three children
    total_weight = kelly_weight + megan_weight + mike_weight

    # Calculate how much too much the three children weigh to cross the bridge
    excess_weight = total_weight - 100

    result = excess_weight
    return result

print(solution())