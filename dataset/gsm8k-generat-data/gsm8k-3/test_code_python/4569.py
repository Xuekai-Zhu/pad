def solution():
    """A rancher owns a mixture of 8 sheep and 5 cattle that graze on his land. In a typical year, the rancher will allow his animals to feed off his pastures for as long as possible before they run out of grass. After the pastures run out of grass, he must buy feed corn for $10 per bag. Each cow eats 2 acres of grass per month, and each sheep eats 1 acre of grass per month. Additionally, a bag of feed corn can feed each cow for 1 month and each sheep for 2 months. If the rancher's pasture contains 144 acres of grass, how much will the rancher need to spend on feed corn to feed his animals each year?"""
    # Define the number of sheep and cattle
    num_sheep = 8
    num_cattle = 5

    # Define the amount of grass each sheep and cattle needs per month
    sheep_grass = 1
    cattle_grass = 2

    # Define the amount of grass available on the rancher's pasture
    pasture_grass = 144

    # Calculate the total amount of grass needed per month
    total_grass = (num_sheep * sheep_grass + num_cattle * cattle_grass)

    # Calculate the number of months the animals can graze on the pasture
    months_grazing = pasture_grass // total_grass

    # Calculate the number of bags of feed corn needed for the remaining months
    remaining_months = 12 - months_grazing
    bags_needed = num_sheep * remaining_months * 2 + num_cattle * remaining_months

    # Calculate the total cost of feed corn needed
    total_cost = bags_needed * 10

    # Display the total cost
    result = total_cost
    return result

print(solution())