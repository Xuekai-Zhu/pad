def solution():
    """Venus is at the deli to get subs for a party. She needs 81 inches of sub. The shop sells 5 and 8 inch subs. If she buys two 8 inch subs, how many 5 inch subs does she need to buy?"""
    total_sub_length = 81
    sub_8in_length = 16  # 2 subs of 8 inches each
    sub_5in_length = total_sub_length - sub_8in_length
    num_5in_subs = sub_5in_length // 5
    result = num_5in_subs
    return result

print(solution())