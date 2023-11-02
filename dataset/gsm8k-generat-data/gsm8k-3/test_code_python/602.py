def solution():
    """A publishing house decides to create a contest for new writers and will award a total of $800 in prizes to the 18 novels with the most votes. First place will get $200, second place will get $150, third place $120 and the rest of the awards will be paid with the same amount of money. How much money will each writer earn from fourth place onwards?"""
    # Define the prize money for first three places
    first_place = 200
    second_place = 150
    third_place = 120

    # Calculate the total prize money for the remaining 15 places
    remaining_prize_money = 800 - (first_place + second_place + third_place)

    # Calculate the prize money for each of the remaining places
    prize_money_per_place = remaining_prize_money / 15

    # Display the prize money for each writer from fourth place onwards
    result = prize_money_per_place
    return result

print(solution())