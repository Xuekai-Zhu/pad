def solution():
    """A rancher owns a mixture of 8 sheep and 5 cattle that graze on his land. In a typical year, the rancher will allow his animals to feed off his pastures for as long as possible before they run out of grass. After the pastures run out of grass, he must buy feed corn for $10 per bag. Each cow eats 2 acres of grass per month, and each sheep eats 1 acre of grass per month. Additionally, a bag of feed corn can feed each cow for 1 month and each sheep for 2 months. If the rancher's pasture contains 144 acres of grass, how much will the rancher need to spend on feed corn to feed his animals each year?"""
    sheep = 8
    cattle = 5
    total_animals = sheep + cattle
    pasture_size = 144
    total_grass_needed = (sheep * 1 + cattle * 2) * 12 # acres of grass needed for a year
    if total_grass_needed <= pasture_size:
        return 0 # no need to buy feed corn
    else:
        corn_needed = (total_grass_needed - pasture_size) / 2
        bags_needed = corn_needed / (sheep * 2 + cattle)
        total_cost = bags_needed * 10
        return total_cost

print(solution())