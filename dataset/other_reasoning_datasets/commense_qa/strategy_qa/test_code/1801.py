def solution():
    new_corporate_identity = "Stellantis"
    fiat_chrysler_brands = ["Fiat", "Chrysler"]
    if new_corporate_identity not in fiat_chrysler_brands:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())