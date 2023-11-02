def solution():
    """The difference in the number of pens that Alice and Clara each have matches their age difference. Alice has 60 pens and Clara has 2/5 times as many pens as Alice. If Alice's age is 20 and Clara is older than Alice, calculate Clara's age in 5 years to come."""
    # Define Alice's age and the number of pens she has
    alice_age = 20
    alice_pens = 60

    # Calculate Clara's number of pens
    clara_pens = alice_pens - alice_age

    # Calculate Clara's current age
    clara_age = clara_pens + alice_age

    # Calculate Clara's age in 5 years
    clara_age_5_years = clara_age + 5

    # return the result
    result = clara_age_5_years
    return result

print(solution())