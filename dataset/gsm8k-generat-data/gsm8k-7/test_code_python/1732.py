def solution():
    num_scoops_per_carton = 10

    # Mary has 3 cartons of ice cream
    mary_cartons = {"chocolate": 1, "strawberry": 1, "vanilla": 1}

    # Ethan wants 1 scoop of vanilla and 1 of chocolate
    ethan_scoops = {"chocolate": 1, "vanilla": 1}

    # Lucas, Danny, and Connor all want 2 scoops of chocolate
    chocolate_scoops = {"Lucas": 2, "Danny": 2, "Connor": 2}
    total_chocolate_scoops = sum(chocolate_scoops.values())

    # Olivia wants a scoop of vanilla and one of strawberry
    olivia_scoops = {"vanilla": 1, "strawberry": 1}

    # Shannon wants twice as much as Olivia
    shannon_scoops = {flavor: 2 * num for flavor, num in olivia_scoops.items()}

    # Calculate the total number of scoops used
    total_scoops_used = sum(ethan_scoops.values()) + total_chocolate_scoops + sum(olivia_scoops.values()) + sum(
        shannon_scoops.values())

    # Calculate the total number of scoops left
    num_scoops_left = (num_scoops_per_carton * len(mary_cartons)) - total_scoops_used
    result = num_scoops_left
    return result

print(solution())