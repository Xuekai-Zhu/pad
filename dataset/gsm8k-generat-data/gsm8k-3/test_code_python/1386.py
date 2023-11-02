def solution():
    """An auto shop buys tires to replace all the tires on every customer’s car. They buy the tires as soon as cars are brought into the shop. There are four cars in the shop already, and another six customers come into the shop throughout the week. Some of the customers decide they don't want any of the tires changing, and two customers decide they only want half the tires changing. They had no tires in stock at the start of the week. If the shop has 20 tires left at the end of the week, how many customers decided they did not want their tires changing?"""
    # Define the number of cars and customers
    initial_cars = 4
    new_customers = 6

    # Calculate the total number of cars
    total_cars = initial_cars + new_customers

    # Calculate the total number of tires needed
    total_tires = total_cars * 4

    # Define the number of customers who don't want their tires changed
    no_change_customers = 2

    # Define the number of tires not needed by customers who don't want their tires changed
    no_change_tires = no_change_customers * 4

    # Define the number of customers who only want half their tires changed
    half_change_customers = 2

    # Define the number of tires not needed by customers who only want half their tires changed
    half_change_tires = half_change_customers * 2

    # Calculate the number of tires actually needed
    needed_tires = total_tires - no_change_tires - half_change_tires - 20

    # Calculate the number of customers who didn't want their tires changed
    no_change_customers = new_customers - (total_tires - needed_tires) // 4

    # Display the number of customers who didn't want their tires changed
    result = no_change_customers
    return result

print(solution())