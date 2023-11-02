def solution():
    # Define Alice's age and number of pens
    alice_age = 20
    alice_pens = 60

    # Calculate Clara's number of pens
    clara_pens = (2/5) * alice_pens

    # Calculate the age difference between Alice and Clara
    age_difference = alice_pens - clara_pens

    # Calculate Clara's current age
    clara_age = alice_age + age_difference

    # Calculate Clara's age in 5 years
    clara_future_age = clara_age + 5
    result = clara_future_age
    return result

print(solution())