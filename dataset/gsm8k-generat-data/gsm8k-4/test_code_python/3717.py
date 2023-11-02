def solution():
    """Mark plants some strawberries in his backyard. Every month, the number of strawberry plants doubles. After 3 months, Mark digs up 4 strawberry plants and gives them to his friend. If he still has 20 strawberry plants, how many did he initially plant?"""
    # Define the number of initial strawberry plants
    initial_plants = None

    # Calculate the number of strawberry plants after 3 months
    plants_after_3_months = 2**3 * initial_plants

    # Calculate the number of strawberry plants given to Mark's friend
    plants_given_away = 4

    # Calculate the number of strawberry plants remaining
    plants_remaining = 20

    # Solve for the initial number of strawberry plants
    initial_plants = (plants_given_away + plants_remaining) / 2**3

    result = round(initial_plants)
    return result

print(solution())