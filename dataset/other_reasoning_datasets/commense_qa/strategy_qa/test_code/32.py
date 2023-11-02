def solution():
    noble_gases = ["He", "Ne", "Ar", "Kr", "Xe", "Rn"]
    argon_index = noble_gases.index("Ar")
    neon_index = noble_gases.index("Ne")
    if argon_index == neon_index + 1 or argon_index == neon_index - 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())