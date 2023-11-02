def solution():
    scoops_per_carton = 10
    total_scoops = 3 * scoops_per_carton  # Mary has 3 cartons of ice cream
    total_scoops -= 1 + 1  # Ethan wants one scoop of vanilla and one of chocolate
    total_scoops -= 2 * 3  # Lucas, Danny, and Connor all want 2 scoops of chocolate
    total_scoops -= 1 + 1  # Olivia would like a scoop of vanilla and one of strawberry
    shannon_scoops = 2 * (1 + 1)  # Shannon wants twice as much as Olivia
    total_scoops -= shannon_scoops

    result = total_scoops
    return result

print(solution())