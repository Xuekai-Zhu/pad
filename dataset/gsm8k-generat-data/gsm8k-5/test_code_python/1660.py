def solution():
    green_papayas = 14  # There are originally 14 green papayas on the tree
    papayas_turned_yellow_friday = 2  # On Friday, 2 papayas turned yellow
    papayas_turned_yellow_sunday = 2 * papayas_turned_yellow_friday  # On Sunday, twice as many papayas as Friday turned yellow

    # Calculate the total number of papayas that turned yellow
    total_papayas_turned_yellow = papayas_turned_yellow_friday + papayas_turned_yellow_sunday

    # Calculate the number of green papayas left on the tree
    green_papayas_left = green_papayas - total_papayas_turned_yellow
    result = green_papayas_left
    return result

print(solution())