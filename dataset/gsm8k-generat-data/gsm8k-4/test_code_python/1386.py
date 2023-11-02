def solution():
    """An auto shop buys tires to replace all the tires on every customer’s car. They buy the tires as soon as cars are brought into the shop. There are four cars in the shop already, and another six customers come into the shop throughout the week. Some of the customers decide they don't want any of the tires changing, and two customers decide they only want half the tires changing. They had no tires in stock at the start of the week. If the shop has 20 tires left at the end of the week, how many customers decided they did not want their tires changing?"""
    # Define the initial number of tires
    initial_tires = 0

    # Define the number of tires needed for each car
    tires_per_car = 4

    # Calculate the number of tires needed for the initial 4 cars
    initial_tires += tires_per_car * 4

    # Calculate the number of tires needed for the additional 6 customers
    for i in range(6):
        # Assume all customers want full tire changes initially
        tires_needed = tires_per_car

        # Two customers only want half the tires changed
        if i == 2 or i == 3:
            tires_needed = tires_per_car / 2

        # Subtract the tires needed from the initial number of tires
        initial_tires -= tires_needed

    # Calculate the number of customers who did not want any tires changed
    no_change_customers = (initial_tires - 20) / tires_per_car

    # Return the result
    result = int(no_change_customers)
    return result

print(solution())