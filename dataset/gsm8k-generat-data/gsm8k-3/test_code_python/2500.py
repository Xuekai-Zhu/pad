def solution():
    """Claire wants to make 2 cakes for her mother. Two packages of flour are required for making a cake. If 1 package of flour is $3, how much does she pay for the flour that is enough to make 2 cakes?"""
    # Define the number of packages of flour required per cake
    PACKAGES_PER_CAKE = 2

    # Define the cost of one package of flour
    FLOUR_PRICE = 3

    # Calculate the total number of packages of flour required
    total_packages = 2 * PACKAGES_PER_CAKE

    # Calculate the total cost of the flour
    total_cost = total_packages * FLOUR_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())