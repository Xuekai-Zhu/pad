def solution():
    paintings_per_day = 2  # Philip makes 2 paintings per day
    starting_paintings = 20  # Philip already has 20 paintings
    days = 30  # Philip wants to know how many paintings he will have after 30 days

    # Calculate the total number of paintings Philip will have after 30 days
    total_paintings = starting_paintings + (paintings_per_day * days)

    result = total_paintings
    return result

print(solution())