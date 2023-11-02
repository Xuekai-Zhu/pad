def solution():
    """Venus is at the deli to get subs for a party. She needs 81 inches of sub. The shop sells 5 and 8 inch subs. If she buys two 8 inch subs, how many 5 inch subs does she need to buy?"""
    total_inches = 81
    eight_inch_subs = 2
    used_inches = eight_inch_subs * 8
    remaining_inches = total_inches - used_inches
    five_inch_subs = remaining_inches // 5
    if remaining_inches % 5 != 0:
        five_inch_subs += 1

    result = five_inch_subs
    return result

print(solution())