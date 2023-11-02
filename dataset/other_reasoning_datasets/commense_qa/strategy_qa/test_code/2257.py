def solution():
    # Define taking ukemi and the relationship between ukemi and kinetic energy
    taking_ukemi = True
    uses_kinetic_energy = True
    # Check if taking ukemi halts kinetic energy
    if taking_ukemi and uses_kinetic_energy:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())