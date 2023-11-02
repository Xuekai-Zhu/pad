def solution():
    # Calculate the total number of cans
    total_cans = 12 + (3 * 12) + 46 + 250  # found 12 cans at home, three times as many at his grandparents' house, neighbor gave 46, dad brought 250 from office

    # Calculate the total amount of money Collin could earn
    total_money = total_cans * 0.25  # Collin could earn $0.25 per aluminum can

    # Calculate the amount of money Collin needs to put into savings
    savings = total_money / 2

    result = savings
    return result

print(solution())