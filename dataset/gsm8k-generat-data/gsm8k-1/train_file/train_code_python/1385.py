def solution():
    """An auto shop buys tires to replace all the tires on every customer’s car. They buy the tires as soon as cars are brought into the shop. There are four cars in the shop already, and another six customers come into the shop throughout the week. Some of the customers decide they don't want any of the tires changing, and two customers decide they only want half the tires changing. They had no tires in stock at the start of the week. If the shop has 20 tires left at the end of the week, how many customers decided they did not want their tires changing?"""
    cars_in_shop = 4
    new_customers = 6
    tires_per_car = 4
    tires_in_stock = 20
    total_customers = cars_in_shop + new_customers
    total_tires_needed = total_customers * tires_per_car
    half_tires_customers = 2
    no_change_customers = total_customers - half_tires_customers - (total_tires_needed - tires_in_stock) // tires_per_car
    result = no_change_customers
    return result

print(solution())