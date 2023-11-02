def solution():
    bulk_carrier_cargo = ["grains", "coal", "ore", "steel coils", "cement"]
    bromine_state = "liquid"
    if bromine_state != "liquid" and bromine_state not in bulk_carrier_cargo:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())