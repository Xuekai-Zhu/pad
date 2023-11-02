def solution():
    grandmother_gift = 20
    aunt_gift = 25
    uncle_gift = 30
    total_gifts = grandmother_gift + aunt_gift + uncle_gift

    starting_amount = total_gifts  # assuming he had no money before
    remaining_amount = starting_amount - (3 * 35)  # subtracting the cost of 3 games
    result = remaining_amount
    return result

print(solution())