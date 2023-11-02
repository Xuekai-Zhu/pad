def solution():
    cups_needed = 6  # Michael needs 6 cups of flour
    measuring_cup = 1/4  # Michael's measuring cup size is 1/4 cup
    total_flour = 8  # Michael has an 8 cup bag of flour

    # Calculate the number of cups of flour he doesn't need
    extra_flour = total_flour - cups_needed

    # Calculate the number of scoops he needs to remove
    scoops_to_remove = int(extra_flour / measuring_cup)

    result = scoops_to_remove
    return result

print(solution())