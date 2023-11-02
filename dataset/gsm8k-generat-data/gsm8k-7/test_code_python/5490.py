def solution():
    num_rabbits = 16

    # Toys bought on Monday
    toys_monday = 6

    # Toys bought on Wednesday
    toys_wednesday = 2 * toys_monday

    # Toys bought on Friday
    toys_friday = 4 * toys_monday

    # Toys bought on Saturday
    toys_saturday = toys_wednesday / 2

    # Total number of toys bought
    total_toys = toys_monday + toys_wednesday + toys_friday + toys_saturday

    # Number of toys per rabbit
    toys_per_rabbit = total_toys / num_rabbits
    result = toys_per_rabbit
    return result

print(solution())