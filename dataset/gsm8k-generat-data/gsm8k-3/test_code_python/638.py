def solution():
    """James buys 200 lotto tickets for 2 dollars each. Of those tickets 20% are winners. 80% of the winners are for 5 dollars. 1 ticket is the grand prize of $5,000. The other tickets win an average of $10. How much did he profit?"""
    # Define the number of tickets and cost per ticket
    NUM_TICKETS = 200
    TICKET_COST = 2

    # Calculate the total cost of the tickets
    total_cost = NUM_TICKETS * TICKET_COST

    # Calculate the number of winning tickets
    num_winners = NUM_TICKETS * 0.2

    # Calculate the number of $5 winners and their total payout
    num_5_winners = num_winners * 0.8
    payout_5_winners = num_5_winners * 5

    # Calculate the total payout of the non-grand prize winners
    total_non_gp_payout = (num_5_winners * 5) + ((num_winners - num_5_winners) * 10)

    # Calculate the total profit from the non-grand prize winners
    total_non_gp_profit = total_non_gp_payout - total_cost

    # Calculate the total profit from the grand prize winner
    gp_profit = 5000 - total_cost

    # Calculate the total profit
    total_profit = total_non_gp_profit + gp_profit

    # Display the total profit
    result = total_profit 
    return result

print(solution())