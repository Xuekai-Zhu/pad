def solution():
    # Calculate the total number of seats in the opera house
    total_seats = 150 * 10

    # Calculate the number of seats that were not taken
    not_taken = 0.2 * total_seats

    # Calculate the number of seats that were taken
    taken = total_seats - not_taken

    # Calculate the total earnings from the show
    earnings = taken * 10
    result = earnings
    return result

print(solution())