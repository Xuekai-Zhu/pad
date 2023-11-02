def solution():
    total_animals = 84  # Jason pepper-sprays 84 animals total
    squirrels_ratio = 6  # Jason pepper-sprays 6 times as many squirrels as raccoons

    # Calculate the number of squirrels pepper-sprayed
    num_squirrels = total_animals / (squirrels_ratio + 1)

    # Calculate the number of raccoons pepper-sprayed
    num_raccoons = squirrels_ratio * num_squirrels
    result = num_raccoons
    return result

print(solution())