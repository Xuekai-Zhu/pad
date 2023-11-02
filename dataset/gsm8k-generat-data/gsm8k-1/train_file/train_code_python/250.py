def solution():
    """One pie costs $4 for a piece. Each pie is having 3 pieces. During one hour the bakery can make 12 pies. Creating one pie costs the bakery $0.5. Considering the bakery would be able to sell all pie pieces, how much money would it make?"""
    cost_per_pie = 0.5
    price_per_piece = 4
    pieces_per_pie = 3
    pies_per_hour = 12
    total_profit = (price_per_piece * pieces_per_pie - cost_per_pie) * pies_per_hour
    result = total_profit
    return result

print(solution())