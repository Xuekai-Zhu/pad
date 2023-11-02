def solution():
    """A carton of ice cream contains 10 scoops each. Mary has 3 cartons of ice cream, one chocolate, one strawberry and one vanilla. Ethan wants one scoop of vanilla and one of chocolate. Lucas, Danny and Connor all want 2 scoops of chocolate. Olivia would like a scoop of vanilla and one of strawberry. Shannon wants twice as much as Olivia. How many scoops of ice cream will be left?"""
    carton_size = 10
    chocolate_cartons = 1
    strawberry_cartons = 1
    vanilla_cartons = 1
    ethan_vanilla = 1
    ethan_chocolate = 1
    lucas_chocolate = 2
    danny_chocolate = 2
    connor_chocolate = 2
    olivia_vanilla = 1
    olivia_strawberry = 1
    shannon = olivia_vanilla + olivia_strawberry * 2
    total_scoops = (chocolate_cartons + strawberry_cartons + vanilla_cartons) * carton_size
    total_scoops -= (ethan_vanilla + ethan_chocolate + lucas_chocolate + danny_chocolate + connor_chocolate + olivia_vanilla + olivia_strawberry + shannon)
    result = total_scoops
    return result

print(solution())