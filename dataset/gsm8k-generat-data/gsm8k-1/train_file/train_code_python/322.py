def solution():
    """Jay & Gloria were hosting a 4th of July party at their house. Jay invited 22 people and Gloria invited 36. They wanted to buy small American flags for everyone. The craft store was having a sale on small flags, 5 flags for $1.00. If they wanted all of their guests to have a flag and they also wanted 1 flag each, how much would they spend at the craft store?"""
    jay_guests = 22
    gloria_guests = 36
    total_guests = jay_guests + gloria_guests
    total_flags = total_guests + 2
    flags_per_sale = 5
    sale_price = 1.00
    total_sales = total_flags / flags_per_sale
    total_cost = total_sales * sale_price
    result = total_cost
    return result

print(solution())