def solution():
    """Mark plants some strawberries in his backyard. Every month, the number of strawberry plants doubles. After 3 months, Mark digs up 4 strawberry plants and gives them to his friend. If he still has 20 strawberry plants, how many did he initially plant?"""
    final_plants = 20
    months = 3
    gifted_plants = 4
    remaining_plants = final_plants + gifted_plants
    initial_plants = remaining_plants // (2**months)
    result = initial_plants
    return result

print(solution())