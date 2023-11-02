def solution():
    """The difference in the number of pens that Alice and Clara each have matches their age difference. Alice has 60 pens and Clara has 2/5 times as many pens as Alice. If Alice's age is 20 and Clara is older than Alice, calculate Clara's age in 5 years to come."""
    alice_age = 20
    alice_pens = 60
    clara_pens = (2/5) * alice_pens
    clara_age_diff = alice_pens - clara_pens
    clara_age = alice_age + clara_age_diff
    clara_age_in_5_years = clara_age + 5
    result = clara_age_in_5_years
    return result

print(solution())