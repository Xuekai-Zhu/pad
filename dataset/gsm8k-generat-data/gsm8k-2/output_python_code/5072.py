def solution():
    """A bakery sells boxes of doughnuts and if there are any doughnuts left at the end of the day, the bakery gives them away. Each box of doughnuts holds 10 doughnuts and all of the doughnuts that the bakery makes are put into these boxes. The bakery makes 300 doughnuts for the day and sells 27 boxes of doughnuts throughout the day. How many doughnuts are given away at the end of the day?"""
    total_doughnuts = 300
    sold_doughnuts = 27 * 10
    leftover_doughnuts = total_doughnuts - sold_doughnuts
    result = leftover_doughnuts
    return result

print(solution())