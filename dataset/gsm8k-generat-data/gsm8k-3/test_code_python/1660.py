def solution():
    """There are 14 green papayas on the papaya tree.  On Friday, two of the fruits turned yellow.  On Sunday, twice as many fruits as on Friday turn yellow.  How many green papayas are left on the tree?"""
    # Define the initial number of papayas
    initial_papayas = 14

    # Calculate the number of papayas that turned yellow on Friday
    friday_yellow = 2

    # Calculate the number of papayas that turned yellow on Sunday
    sunday_yellow = 2 * friday_yellow

    # Calculate the remaining number of green papayas
    remaining_papayas = initial_papayas - friday_yellow - sunday_yellow

    # Display the remaining number of green papayas
    result = remaining_papayas
    return result

print(solution())