def solution():
    bob_money = 60  # Bob has $60 in his account
    phil_money = bob_money / 3  # Phil has one-third of what Bob has
    jenna_money = 2 * phil_money  # Jenna has twice as much as Phil

    # Calculate how much less Jenna has than Bob
    difference = bob_money - jenna_money
    result = difference
    return result

print(solution())