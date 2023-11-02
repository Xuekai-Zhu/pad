def solution():
    """The Lion King cost 10 million to make and earned 200 million at the box office. If it earned a profit that was half of what Star Wars made and Star Wars cost 25 million to make, how many millions did Star Wars earn?"""
    lion_king_cost = 10
    lion_king_earnings = 200
    lion_king_profit = lion_king_earnings - lion_king_cost
    star_wars_cost = 25
    star_wars_profit = 2 * lion_king_profit
    star_wars_earnings = star_wars_profit + star_wars_cost
    result = star_wars_earnings
    return result

print(solution())