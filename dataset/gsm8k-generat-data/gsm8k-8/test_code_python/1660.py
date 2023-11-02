def solution():
    # Define the number of green papayas
    green_papayas = 14

    # Determine how many papayas turn yellow on Friday
    friday_yellow = 2

    # Determine how many papayas turn yellow on Sunday (twice as many as on Friday)
    sunday_yellow = 2 * friday_yellow

    # Subtract the yellow papayas from the total to find the remaining green papayas
    remaining_papayas = green_papayas - friday_yellow - sunday_yellow

    result = remaining_papayas
    return result

print(solution())