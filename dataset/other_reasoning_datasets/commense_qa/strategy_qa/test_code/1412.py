def solution():
    common_carp = True
    invasive_species = True
    tolerant_of_conditions = True
    able_to_survive_frozen_waters = True
    able_to_survive_low_oxygenated_waters = True
    if common_carp and invasive_species and tolerant_of_conditions and able_to_survive_frozen_waters and able_to_survive_low_oxygenated_waters:
        result = "no, they are not sensitive"
    else:
        result = "yes, they are sensitive"
    return result

print(solution())