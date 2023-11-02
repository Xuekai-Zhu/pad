def solution():
    """A bakery sells boxes of doughnuts and if there are any doughnuts left at the end of the day, the bakery gives them away. Each box of doughnuts holds 10 doughnuts and all of the doughnuts that the bakery makes are put into these boxes. The bakery makes 300 doughnuts for the day and sells 27 boxes of doughnuts throughout the day. How many doughnuts are given away at the end of the day?"""
    # Define the number of doughnuts per box
    DOUGHNUTS_PER_BOX = 10

    # Calculate the total number of boxes sold
    boxes_sold = 27

    # Calculate the total number of doughnuts sold
    doughnuts_sold = boxes_sold * DOUGHNUTS_PER_BOX

    # Calculate the number of doughnuts left at the end of the day
    doughnuts_left = 300 - doughnuts_sold

    # If there are no doughnuts left, return 0
    if doughnuts_left <= 0:
        return 0

    # If there are doughnuts left, calculate the number given away
    else:
        doughnuts_given_away = doughnuts_left
        return doughnuts_given_away

print(solution())