def solution():
    """Mark plants some strawberries in his backyard. Every month, the number of strawberry plants doubles. After 3 months, Mark digs up 4 strawberry plants and gives them to his friend. If he still has 20 strawberry plants, how many did he initially plant?"""
    final_strawberry_plants = 20
    months_since_planting = 3
    strawberries_given_away = 4
    remaining_strawberry_plants = final_strawberry_plants + strawberries_given_away
    for i in range(months_since_planting):
        remaining_strawberry_plants /= 2
    initial_strawberry_plants = remaining_strawberry_plants + strawberries_given_away
    result = initial_strawberry_plants
    return result

print(solution())