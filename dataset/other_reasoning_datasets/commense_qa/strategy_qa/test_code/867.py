def solution():
    # Define the properties of isopropyl alcohol and salt
    salt_solubility = "high"
    isopropyl_alcohol = "unique"
    # Check if salt has low solubility in isopropyl alcohol
    if isopropyl_alcohol == "unique" and salt_solubility == "low":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())