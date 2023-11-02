def solution():
    initial_rice = 50  # kilograms of rice
    stored_rice = (7/10) * initial_rice  # kilograms of rice kept in storage
    given_rice = initial_rice - stored_rice  # kilograms of rice given to Mr. Everest
    difference = stored_rice - given_rice  # difference in kilograms of rice kept by Mr. Llesis and given to Mr. Everest
    result = difference
    return result

print(solution())