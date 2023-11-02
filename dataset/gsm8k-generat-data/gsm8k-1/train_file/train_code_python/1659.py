def solution():
    """There are 14 green papayas on the papaya tree. On Friday, two of the fruits turned yellow. On Sunday, twice as many fruits as on Friday turn yellow. How many green papayas are left on the tree?"""
    initial_papayas = 14
    friday_yellow = 2
    sunday_yellow = 2 * friday_yellow
    remaining_papayas = initial_papayas - (friday_yellow + sunday_yellow)
    result = remaining_papayas
    return result

print(solution())