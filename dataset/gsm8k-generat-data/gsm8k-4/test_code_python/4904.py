def solution():
    """The Lion King cost 10 million to make and earned 200 million at the box office. If it earned a profit that was half of what Star Wars made and Star Wars cost 25 million to make, how many millions did Star Wars earn?"""
    # Define the cost and revenue of The Lion King
    lion_king_cost = 10
    lion_king_revenue = 200

    # Calculate the profit of The Lion King
    lion_king_profit = lion_king_revenue - lion_king_cost

    # Define the cost of Star Wars
    star_wars_cost = 25

    # Calculate the profit of Star Wars based on the profit of The Lion King
    star_wars_profit = 2 * lion_king_profit

    # Calculate the revenue of Star Wars based on its profit and cost
    star_wars_revenue = star_wars_profit + star_wars_cost

    # Return the revenue of Star Wars in millions
    result = star_wars_revenue
    return result

print(solution())