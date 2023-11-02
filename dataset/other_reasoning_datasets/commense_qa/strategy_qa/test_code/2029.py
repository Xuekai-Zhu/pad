def solution():
    # Define Han Solo's age and citizenship status
    han_solo_age = 36
    han_solo_citizenship = "not American"
    # Check if Han Solo meets the age and citizenship requirements for the US Air Force
    if han_solo_age < 18 or han_solo_age > 35 or han_solo_citizenship != "American":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())