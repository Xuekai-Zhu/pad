def solution():
    # Calculate the total number of seats in the opera house
    total_seats = 150 * 10

    # Calculate the number of seats that were not taken
    not_taken = round(total_seats * 0.2)

    # Calculate the total earnings from the show
    earnings = (total_seats - not_taken) * 10
    result = earnings
    return result

print(solution())