def solution():
    """A carton of ice cream contains 10 scoops each. Mary has 3 cartons of ice cream, one chocolate, one strawberry and one vanilla. Ethan wants one scoop of vanilla and one of chocolate. Lucas, Danny and Connor all want 2 scoops of chocolate. Olivia would like a scoop of vanilla and one of strawberry. Shannon wants twice as much as Olivia. How many scoops of ice cream will be left?"""
    # Define the number of scoops per carton and the number of cartons for each flavor
    SCOOPS_PER_CARTON = 10
    CHOCOLATE_CARTONS = 1
    STRAWBERRY_CARTONS = 1
    VANILLA_CARTONS = 1

    # Define the number of scoops each person wants
    ETHAN_SCOOPS = 2
    LUCAS_SCOOPS = 2
    DANNY_SCOOPS = 2
    CONNOR_SCOOPS = 2
    OLIVIA_SCOOPS = 2
    SHANNON_SCOOPS = 4

    # Calculate the total number of scoops
    total_scoops = SCOOPS_PER_CARTON * (CHOCOLATE_CARTONS + STRAWBERRY_CARTONS + VANILLA_CARTONS)

    # Remove the scoops that Ethan wants
    total_scoops -= ETHAN_SCOOPS

    # Remove the scoops that Lucas, Danny, and Connor want
    total_scoops -= LUCAS_SCOOPS * 2
    total_scoops -= DANNY_SCOOPS * 2
    total_scoops -= CONNOR_SCOOPS * 2

    # Remove the scoops that Olivia and Shannon want
    total_scoops -= OLIVIA_SCOOPS
    total_scoops -= SHANNON_SCOOPS

    # return the result
    result = total_scoops
    return result

print(solution())