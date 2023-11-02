def solution():
    fair_tickets_sold = 25  # Given that 25 fair tickets were sold
    # Let x be the number of baseball tickets sold
    # According to the problem, 2 times the number of baseball tickets sold plus 6 is equal to the number of fair tickets sold
    # 2x + 6 = fair_tickets_sold
    # Solving for x gives x = (fair_tickets_sold - 6) / 2
    baseball_tickets_sold = (fair_tickets_sold - 6) / 2
    result = baseball_tickets_sold
    return result

print(solution())