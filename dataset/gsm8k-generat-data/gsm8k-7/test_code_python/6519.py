def solution():
    starting_snails = 3
    additional_snails = 2
    num_days = 5

    # Calculate the total number of snails eaten over the 5 days
    total_snails_eaten = starting_snails
    for day in range(1, num_days):
        additional_snails_eaten = starting_snails + (day * additional_snails)
        total_snails_eaten += additional_snails_eaten

    result = total_snails_eaten
    return result

print(solution())