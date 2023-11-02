def solution():
    """Lily has 5 lottery tickets to sell. She sells the first ticket for $1. She then sells each successive ticket for a dollar more than the previous ticket. She plans to keep a $4 profit and give the remaining money as the prize. How much money will the winner of the lottery receive?"""
    # Define the total number of tickets and the initial price
    total_tickets = 5
    initial_price = 1

    # Calculate the sum of prices for all tickets sold
    ticket_prices = [initial_price + i for i in range(total_tickets)]
    total_price = sum(ticket_prices)

    # Calculate the total earnings for Lily, including her $4 profit
    total_earnings = total_price + 4

    # Calculate the prize for the winner
    winner_prize = (total_earnings - 4) / 2

    # return the result
    result = winner_prize
    return result

print(solution())