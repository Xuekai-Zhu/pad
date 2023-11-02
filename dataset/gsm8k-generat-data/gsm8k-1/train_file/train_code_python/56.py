def solution():
    """Liza bought 10 kilograms of butter to make cookies. She used one-half of it for chocolate chip cookies, one-fifth of it for peanut butter cookies, and one-third of the remaining butter for sugar cookies. How many kilograms of butter are left after making those three kinds of cookies?"""
    total_butter = 10
    butter_used_cc = total_butter / 2
    butter_used_pb = total_butter / 5
    butter_remaining = total_butter - butter_used_cc - butter_used_pb
    butter_used_sc = butter_remaining / 3
    butter_remaining -= butter_used_sc
    result = butter_remaining
    return result

print(solution())