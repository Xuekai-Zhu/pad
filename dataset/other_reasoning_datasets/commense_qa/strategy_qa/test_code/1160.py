def solution():
    achilles_companions = ["Ajax", "Odysseus"]
    legolas_companions = ["Gandalf"]
    achilles_weakness = "heel"
    # Check if Legolas is capable of exploiting Achilles's weakness
    if achilles_weakness in legolas_companions:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())