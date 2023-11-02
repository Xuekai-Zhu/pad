def solution():
    """Josh gets together with 7 friends.  Everyone including him puts 5 dollars into a pot.  First place gets 80% of the money.  Second and third place split the rest.  How much money does third place get?"""
    # Calculate the total amount of money in the pot
    total_money = 8 * 5

    # Calculate the first place prize
    first_place_prize = total_money * 0.8

    # Calculate the remaining prize money
    remaining_prize_money = total_money - first_place_prize

    # Split the remaining prize money between second and third place
    second_third_prize = remaining_prize_money / 2

    # Third place gets half of the remaining prize money
    third_place_prize = second_third_prize / 2

    result = third_place_prize
    return result

print(solution())