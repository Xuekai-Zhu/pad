def solution():
    distance = 5000
    popcorn_per_feet = 1/25
    squirrel_eat = 1/4

    # Calculate the total popcorn Jenny dropped on her way home
    total_popcorn_dropped = distance * popcorn_per_feet

    # Calculate the amount of popcorn eaten by the squirrel
    popcorn_eaten = squirrel_eat * total_popcorn_dropped

    # Calculate the remaining popcorn on the ground
    remaining_popcorn = total_popcorn_dropped - popcorn_eaten

    result = remaining_popcorn
    return result

print(solution())