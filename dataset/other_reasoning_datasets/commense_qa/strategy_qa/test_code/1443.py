def solution():
    taking_oath_in_court = True
    lying_under_oath = False
    perjury_is_a_crime = True
    if taking_oath_in_court and lying_under_oath and perjury_is_a_crime:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())