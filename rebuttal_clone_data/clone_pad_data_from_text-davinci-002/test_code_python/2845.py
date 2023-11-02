def solution():
    drops_per_feed = 20
    drops_per_liter = 5000
    liters_to_die = 3
    total_drops_to_die = drops_per_liter * liters_to_die
    total_mosquitoes = total_drops_to_die / drops_per_feed
    result = total_mosquitoes
    return result

print(solution())