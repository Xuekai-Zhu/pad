def solution():
    """Cappuccinos cost $2, iced teas cost $3, cafe lattes cost $1.5 and espressos cost $1 each. Sandy orders some drinks for herself and some friends. She orders three cappuccinos, two iced teas, two cafe lattes, and two espressos. How much change does she receive back for a twenty-dollar bill?"""
    # Define the cost of each drink
    CAPPUCCINO_PRICE = 2
    ICED_TEA_PRICE = 3
    LATTE_PRICE = 1.5
    ESPRESSO_PRICE = 1

    # Define the number of each drink ordered
    cappuccinos = 3
    iced_teas = 2
    cafe_lattes = 2
    espressos = 2

    # Calculate the total cost of the order
    total_cost = (cappuccinos * CAPPUCCINO_PRICE) + (iced_teas * ICED_TEA_PRICE) + (cafe_lattes * LATTE_PRICE) + (
                espressos * ESPRESSO_PRICE)

    # Calculate the change
    change = 20 - total_cost

    # Display the change
    result = change
    return result

print(solution())