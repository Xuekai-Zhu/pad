def solution():
    alice_pens = 60  # Alice has 60 pens
    alice_age = 20  # Alice is 20 years old
    clara_pens = 2/5 * alice_pens  # Clara has 2/5 times as many pens as Alice
    age_difference = alice_age - (clara_pens - alice_pens)  # The age difference is equal to the difference in number of pens

    # Calculate Clara's age in 5 years
    clara_age_in_5_years = age_difference + 5
    result = clara_age_in_5_years
    return result

print(solution())