def solution():
    """Simon and Peter have a big stamp collection. Simon collects red stamps and Peter collects white stamps. Simon has 30 red stamps and Peter has 80 white stamps. If the red stamps are then sold for 50 cents each and the white stamps are sold for 20 cents each, what is the difference in the amount of money they make in dollars?"""
    simon_red_stamps = 30
    peter_white_stamps = 80
    red_stamp_price = 0.5
    white_stamp_price = 0.2
    simon_earnings = simon_red_stamps * red_stamp_price
    peter_earnings = peter_white_stamps * white_stamp_price
    difference = simon_earnings - peter_earnings
    result = difference
    return result

print(solution())