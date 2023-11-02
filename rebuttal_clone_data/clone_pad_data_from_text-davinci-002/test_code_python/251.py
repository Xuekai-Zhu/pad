def solution():
    """One pie costs $4 for a piece. Each pie is having 3 pieces. During one hour the bakery can make 12 pies. Creating one pie costs the bakery $0.5. Considering the bakery would be able to sell all pie pieces, how much money would it make?"""
    cost_per_pie = 4
    pieces_per_pie = 3
    pies_per_hour = 12
    cost_per_pie = 0.5
    total_sales = cost_per_pie * pieces_per_pie * pies_per_hour
    result = total_sales
    return result

print(solution())