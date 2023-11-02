def solution():
    """A publishing house decides to create a contest for new writers and will award a total of $800 in prizes to the 18 novels with the most votes.
    First place will get $200, second place will get $150, third place $120 and the rest of the awards will be paid with the same amount of money.
    How much money will each writer earn from fourth place onwards?"""
    # Define the total amount of prize money
    total_prize_money = 800

    # Define the prize money for first, second and third place
    first_place = 200
    second_place = 150
    third_place = 120

    # Calculate the remaining prize money
    remaining_prize_money = total_prize_money - first_place - second_place - third_place

    # Calculate the number of writers who will receive the remaining prize money
    remaining_writers = 18 - 3

    # Calculate the prize money each writer will receive from fourth place onwards
    prize_money = remaining_prize_money / remaining_writers

    result = prize_money
    return result

print(solution())