def solution():
    """Drew is 5 years older than Maya. Peter is 4 years older than Drew. John is 30 and is twice as old as Maya. In 2 years, Jacob will be exactly half of Peter’s age. How old is Jacob now?"""
    # Let's use variables to represent the ages of the four people
    # Let x be Maya's age
    x = 30/2
    # Drew is 5 years older than Maya
    d = x + 5
    # Peter is 4 years older than Drew
    p = d + 4
    # Jacob's age in 2 years will be half of Peter's age, so let's use y for Jacob's age now
    y = p - 2 - 0.5*2

    # Display Jacob's age
    result = y
    return result

print(solution())