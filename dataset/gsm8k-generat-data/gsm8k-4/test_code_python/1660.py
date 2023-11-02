def solution():
    """There are 14 green papayas on the papaya tree. On Friday, two of the fruits turned yellow. On Sunday, twice as many fruits as on Friday turn yellow. How many green papayas are left on the tree?"""
    # Define the initial number of green papayas
    green_papayas = 14

    # Calculate the number of papayas turning yellow on Friday
    yellow_friday = 2

    # Calculate the number of papayas turning yellow on Sunday
    yellow_sunday = yellow_friday * 2

    # Calculate the remaining number of green papayas
    green_remaining = green_papayas - yellow_friday - yellow_sunday

    # Return the result
    result = green_remaining
    return result

print(solution())