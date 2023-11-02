def solution():
    """The Lion King cost 10 million to make and earned 200 million at the box office. If it earned a profit that was half of what Star Wars made and Star Wars cost 25 million to make, how many millions did Star Wars earn?"""
    # Calculate the profit made by The Lion King
    lion_king_profit = 200 - 10

    # Calculate the profit made by Star Wars
    star_wars_profit = lion_king_profit * 2

    # Calculate the cost of making Star Wars
    star_wars_cost = 25

    # Calculate the earnings made by Star Wars
    star_wars_earnings = star_wars_cost + star_wars_profit

    # Display the earnings made by Star Wars
    result = star_wars_earnings
    return result

print(solution())