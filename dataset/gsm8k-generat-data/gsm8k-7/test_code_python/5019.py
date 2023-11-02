def solution():
    num_suckers_sienna = 2 * num_suckers_bailey
    num_suckers_jen = num_suckers_sienna / 2
    num_suckers_molly = (num_suckers_jen / 2) - 2
    num_suckers_harmony = num_suckers_molly
    num_suckers_taylor = num_suckers_harmony - 1
    num_suckers_callie = 5

    # Jen ate half of Sienna's suckers
    result = num_suckers_jen
    return result

print(solution())