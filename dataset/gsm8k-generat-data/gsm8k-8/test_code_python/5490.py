def solution():
    # Define the number of rabbits and toys
    num_rabbits = 16
    monday_toys = 6
    wednesday_toys = 2 * monday_toys
    friday_toys = 4 * monday_toys
    saturday_toys = 0.5 * wednesday_toys

    # Calculate the total number of toys
    total_toys = monday_toys + wednesday_toys + friday_toys + saturday_toys

    # Calculate the number of toys per rabbit
    toys_per_rabbit = total_toys / num_rabbits

    result = toys_per_rabbit
    return result

print(solution())