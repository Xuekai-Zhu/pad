def solution():
    duck_price = 10
    chicken_price = 8
    num_chickens_sold = 5

    # Calculate the earnings from selling chickens
    earnings_from_chickens = num_chickens_sold * chicken_price

    # Calculate the total earnings, assuming the rest sold were ducks
    total_earnings = earnings_from_chickens + (num_ducks_sold * duck_price)

    # Calculate the amount spent on the new wheelbarrow
    wheelbarrow_cost = total_earnings / 2

    # Calculate the amount earned by selling the wheelbarrow
    wheelbarrow_earnings = wheelbarrow_cost + 60

    # Calculate the cost of the wheelbarrow
    wheelbarrow_cost = wheelbarrow_earnings / 2

    # Calculate the number of ducks sold
    num_ducks_sold = (total_earnings - wheelbarrow_earnings) / duck_price
    result = num_ducks_sold
    return result

print(solution())