def solution():
    # Define the initial amount of money Sid had
    initial_money = 48

    # Calculate half of his initial money plus $4
    remaining_money = 0.5 * initial_money + 4

    # Calculate how much money Sid spent on snacks
    snack_cost = 8

    # Calculate how much money Sid has left after buying snacks
    remaining_money -= snack_cost

    # Calculate how much money Sid spent on computer accessories
    computer_cost = initial_money - remaining_money

    result = computer_cost
    return result

print(solution())