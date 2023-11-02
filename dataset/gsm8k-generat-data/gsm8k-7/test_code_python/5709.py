def solution():
    cloves_per_vampire = 3 / 2
    cloves_per_bat = 3 / 8
    cloves_per_wight = 3 / 3

    num_vampires = 30
    num_wights = 12
    num_bats = 40

    total_cloves = (num_vampires * cloves_per_vampire) + (num_wights * cloves_per_wight) + (num_bats * cloves_per_bat)
    result = total_cloves
    return result

print(solution())