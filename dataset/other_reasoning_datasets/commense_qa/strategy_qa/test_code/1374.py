def solution():
    # Define the tribes that are part of the Four Mothers Society
    four_mothers_tribes = ["Muscogee Creek", "Cherokee", "Choctaw", "Chickasaw"]
    # Check if the Cherokee tribe is part of the Four Mothers Society
    if "Cherokee" in four_mothers_tribes:
        # Check if the delegation sent by the Four Mothers Society opposed allotment
        if (1906 >= 1898 and 1906 < 1902) or (1906 >= 1906 and 1906 < 1934):
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())