def solution():
    hypertension = True
    high_salt_diet = True
    pickles_per_dozen = 12
    salt_content_per_pickle = 500 # mg of sodium
    total_salt_content = pickles_per_dozen * salt_content_per_pickle # mg of sodium in a dozen pickles
    if hypertension and high_salt_diet and total_salt_content < 2300: # recommended daily intake of sodium for hypertension patients
        result = "yes"
    else:
        result = "no"
    return result

print(solution())