def solution():
    # Define the age differences based on birth month
    jolyn_therese_diff = 2
    therese_aivo_diff = 5
    aivo_leon_diff = 2

    # Calculate Aivo's age based on his difference with Leon
    aivo_age = aivo_leon_diff + 0

    # Calculate Therese's age based on her difference with Aivo
    therese_age = therese_aivo_diff + aivo_age

    # Calculate Jolyn's age based on her difference with Therese
    jolyn_age = jolyn_therese_diff + therese_age

    # Calculate the age difference between Jolyn and Leon
    jolyn_leon_diff = jolyn_age - (aivo_age + aivo_leon_diff)

    result = jolyn_leon_diff
    return result

print(solution())