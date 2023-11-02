def solution():
    """The difference in the number of pens that Alice and Clara each have matches their age difference. Alice has 60 pens and Clara has 2/5 times as many pens as Alice. If Alice's age is 20 and Clara is older than Alice, calculate Clara's age in 5 years to come."""
    alice_age = 20
    alice_pens = 60
    clara_pens = (2/5)*alice_pens
    pen_difference = alice_pens - clara_pens
    age_difference = pen_difference
    clara_age = alice_age + age_difference
    
    # calculate Clara's age in 5 years
    clara_age_in_5_years = clara_age + 5
    
    return clara_age_in_5_years

print(solution())