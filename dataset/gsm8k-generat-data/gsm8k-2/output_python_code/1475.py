def solution():
    """A small, old, wooden bridge can hold up to 100 kilograms at once. Mike, Megan, and Kelly are three children who decided to cross the bridge at the same time. Kelly weighs 34 kilograms, which is 15% less than Megan. Mike weighs 5 kilograms more than Megan. How much too much do the three children weigh together to cross the bridge?"""
    max_weight = 100
    kelly_weight = 34
    megan_weight = kelly_weight / 0.85
    mike_weight = megan_weight + 5
    total_weight = kelly_weight + megan_weight + mike_weight
    excess_weight = total_weight - max_weight
    result = excess_weight
    return result

print(solution())