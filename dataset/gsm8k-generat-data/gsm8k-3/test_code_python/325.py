def solution():
    """Jay & Gloria were hosting a 4th of July party at their house.  Jay invited 22 people and Gloria invited 36.  They wanted to buy small American flags for everyone.  The craft store was having a sale on small flags, 5 flags for $1.00.  If they wanted all of their guests to have a flag and they also wanted 1 flag each, how much would they spend at the craft store?"""
    # Calculate the total number of guests
    total_guests = 22 + 36

    # Calculate the total number of flags needed
    total_flags = total_guests + 2

    # Calculate the total number of flag packs needed, accounting for the sale
    flag_packs = total_flags // 5
    if total_flags % 5 > 0:
        flag_packs += 1

    # Calculate the total cost of the flag packs
    total_cost = flag_packs * 1.00

    # Display the total cost
    result = total_cost
    return result

print(solution())