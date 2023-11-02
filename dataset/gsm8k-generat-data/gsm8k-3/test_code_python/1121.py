def solution():
    """The difference in the number of pens that Alice and Clara each have matches their age difference. Alice has 60 pens and Clara has 2/5 times as many pens as Alice. If Alice's age is 20 and Clara is older than Alice, calculate Clara's age in 5 years to come."""
    # Define Alice's age and number of pens
    alice_age = 20
    alice_pens = 60

    # Calculate Clara's number of pens
    clara_pens = (2/5) * alice_pens

    # Calculate the age difference between Alice and Clara
    age_difference = alice_pens - clara_pens

    # Calculate Clara's age in 5 years
    clara_age_in_5_years = alice_age + age_difference + 5

    # Display Clara's age in 5 years
    result = clara_age_in_5_years
    return result

print(solution())