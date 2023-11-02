def solution():
    """A bakery sells boxes of doughnuts and if there are any doughnuts left at the end of the day, the bakery gives them away. Each box of doughnuts holds 10 doughnuts and all of the doughnuts that the bakery makes are put into these boxes. The bakery makes 300 doughnuts for the day and sells 27 boxes of doughnuts throughout the day. How many doughnuts are given away at the end of the day?"""
    # Define the number of doughnuts and boxes
    doughnuts = 300
    boxes = 27

    # Calculate the number of doughnuts sold
    sold = boxes * 10

    # Calculate the number of doughnuts given away
    given_away = doughnuts - sold

    result = given_away
    return result

print(solution())