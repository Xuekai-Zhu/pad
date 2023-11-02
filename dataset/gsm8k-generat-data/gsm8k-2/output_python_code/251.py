def solution():
    """One pie costs $4 for a piece. Each pie is having 3 pieces. During one hour the bakery can make 12 pies. Creating one pie costs the bakery $0.5. Considering the bakery would be able to sell all pie pieces, how much money would it make?"""
    pie_price = 4 
    pie_cost = 0.5
    pie_pieces = 3
    pies_per_hour = 12
    
    total_pie_pieces = pies_per_hour * pie_pieces
    total_pie_cost = pies_per_hour * pie_cost
    total_profit = total_pie_pieces * pie_price - total_pie_cost
    
    result = total_profit
    return result

print(solution())