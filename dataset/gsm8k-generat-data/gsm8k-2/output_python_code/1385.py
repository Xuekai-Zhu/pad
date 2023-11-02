def solution():
    """An auto shop buys tires to replace all the tires on every customer’s car. They buy the tires as soon as cars are brought into the shop. There are four cars in the shop already, and another six customers come into the shop throughout the week. Some of the customers decide they don't want any of the tires changing, and two customers decide they only want half the tires changing. They had no tires in stock at the start of the week. If the shop has 20 tires left at the end of the week, how many customers decided they did not want their tires changing?"""
    total_customers = 4 + 6
    total_tires_needed = total_customers * 4
    half_tires_customers = 2
    no_change_customers = x
    half_tires_count = half_tires_customers * 2
    no_change_count = no_change_customers * 4
    total_tires_bought = total_tires_needed - half_tires_count - no_change_count + 20
    no_change_customers = (total_tires_needed - total_tires_bought) / 4
    result = no_change_customers
    return result

print(solution())