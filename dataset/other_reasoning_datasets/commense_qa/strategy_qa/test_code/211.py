def solution():
    pizza_toppings = ["pepperoni", "sausage", "bacon", "meatball", "anchovies"]
    black_sea_animals = ["dogfish", "jellyfish", "anchovies"]
    overlap = [animal for animal in pizza_toppings if animal in black_sea_animals]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())