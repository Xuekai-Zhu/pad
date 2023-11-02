def solution():
    # Define Thomas's age and the age difference between Shay and Thomas
    thomas_age = 6
    shay_age_difference = 13

    # Calculate Shay's and James's ages
    shay_age = thomas_age + shay_age_difference
    james_age = shay_age + 5

    # Calculate how many years it will take for Thomas to reach his current age
    years_to_reach_current_age = thomas_age

    # Calculate how many years it will take for James to be the same age as Shay is now
    years_for_james_to_catch_up = james_age - shay_age

    # Calculate how old James will be when Thomas reaches his current age
    james_age_when_thomas_reaches_current_age = james_age + years_to_reach_current_age - years_for_james_to_catch_up
    result = james_age_when_thomas_reaches_current_age
    return result

print(solution())