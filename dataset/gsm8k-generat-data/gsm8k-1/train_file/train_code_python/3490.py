def solution():
    """Half of Taylor's house guests like weak coffee and the other half like strong coffee in the morning.
    Taylor uses 1 tablespoon of coffee per cup of water to make it weak and he doubles that amount to make it strong.
    If he makes 12 cups of both weak and strong coffee, how many tablespoons of coffee will he need?"""
    
    guests = 12
    weak_coffee = guests / 2
    strong_coffee = guests / 2
    tablespoons_per_cup_weak = 1
    tablespoons_per_cup_strong = tablespoons_per_cup_weak * 2
    total_tablespoons = (weak_coffee * tablespoons_per_cup_weak) + (strong_coffee * tablespoons_per_cup_strong)
    result = total_tablespoons
    return result

print(solution())