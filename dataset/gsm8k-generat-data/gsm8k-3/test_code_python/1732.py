def solution():
    """A carton of ice cream contains 10 scoops each.  Mary has 3 cartons of ice cream, one chocolate, one strawberry and one vanilla.  Ethan wants one scoop of vanilla and one of chocolate.  Lucas, Danny and Connor all want 2 scoops of chocolate.  Olivia would like a scoop of vanilla and one of strawberry.  Shannon wants twice as much as Olivia.  How many scoops of ice cream will be left?"""
    # Define the number of scoops per carton of ice cream
    SCOOPS_PER_CARTON = 10

    # Define the number of scoops each person wants
    ethan_vanilla = 1
    ethan_chocolate = 1
    lucas_chocolate = 2
    danny_chocolate = 2
    connor_chocolate = 2
    olivia_vanilla = 1
    olivia_strawberry = 1
    shannon_vanilla = 2
    shannon_strawberry = 2

    # Calculate the total number of scoops taken
    total_scoops = ethan_vanilla + ethan_chocolate + (lucas_chocolate * 3) + (danny_chocolate * 3) + (connor_chocolate * 3) + olivia_vanilla + olivia_strawberry + (shannon_vanilla * 2) + (shannon_strawberry * 2)

    # Calculate the total number of scoops in the three cartons
    total_carton_scoops = SCOOPS_PER_CARTON * 3

    # Calculate the number of scoops left
    scoops_left = total_carton_scoops - total_scoops

    # Display the number of scoops left
    result = scoops_left
    return result

print(solution())