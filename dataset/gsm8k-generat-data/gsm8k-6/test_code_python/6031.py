def solution():
    # Find Drew's age
    age_Drew = 2*Sam_age

    # Find the combined age of Sam and Drew
    combined_age = Sam_age + age_Drew

    # Find the value of Sam's age
    Sam_age = combined_age/3

    result = Sam_age
    return result

print(solution())