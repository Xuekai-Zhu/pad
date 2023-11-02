def solution():
    num_carpenters = 8
    num_chairs = 50
    num_days = 10

    # Calculate the productivity of each carpenter
    productivity = num_chairs / (num_carpenters * num_days)

    # Calculate the number of carpenters needed to make 75 chairs in 10 days
    num_chairs_needed = 75
    num_carpenters_needed = num_chairs_needed / (productivity * num_days)
    result = num_carpenters_needed
    return result

print(solution())