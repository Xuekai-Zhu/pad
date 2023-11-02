def solution():
    firewall_protects_attacks = True
    short_circuit_causes_blue_screen = True
    if firewall_protects_attacks and not short_circuit_causes_blue_screen:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())