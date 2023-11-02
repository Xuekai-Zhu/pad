def solution():
    graphics_cards = 10
    hard_drives = 14
    CPUs = 8
    pairs_of_RAM = 4
    graphics_cards_cost = 600
    hard_drives_cost = 80
    CPUs_cost = 200
    pairs_of_RAM_cost = 60
    total_earnings = (graphics_cards * graphics_cards_cost) + (hard_drives * hard_drives_cost) + (CPUs * CPUs_cost) + (pairs_of_RAM * pairs_of_RAM_cost)
    result = total_earnings
    return result

print(solution())