def solution():
    cups_flour = 3  # Mitch needs 3 cups of flour
    cups_sugar = 2  # Mitch needs 2 cups of sugar
    scoop_size = 1/3  # Mitch only has a 1/3 cup scoop

    # Calculate the number of scoops for flour and sugar
    scoops_flour = cups_flour / scoop_size
    scoops_sugar = cups_sugar / scoop_size

    # Calculate the total number of scoops needed
    total_scoops = scoops_flour + scoops_sugar
    result = total_scoops
    return result

print(solution())