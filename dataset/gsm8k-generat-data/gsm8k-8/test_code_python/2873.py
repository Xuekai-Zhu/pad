def solution():
    # Define the number of toddlers and teenagers
    toddlers = 6
    teenagers = 5 * toddlers

    # Define the total number of children
    total_children = toddlers + teenagers + 40  # Newborns included

    # Calculate the number of newborns
    newborns = total_children - (toddlers + teenagers)

    result = newborns
    return result

print(solution())