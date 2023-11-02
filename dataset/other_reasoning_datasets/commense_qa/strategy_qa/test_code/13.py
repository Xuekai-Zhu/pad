def solution():
    Doctor_travel_method = "TARDIS"
    Gateway_travel_method = "wormholes"
    Doctor_reliability = "largely unreliable"
    if Doctor_travel_method != Gateway_travel_method and Doctor_reliability == "largely unreliable":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())