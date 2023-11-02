def solution():
    velvet_price_per_yard = 24  # The price of the velvet fabric per yard is $24
    pattern_price = 15  # The price of the pattern he bought is $15
    thread_price_per_spool = 3  # The price of each spool of silver thread is $3
    total_spools_of_thread = 2  # Louis bought two spools of silver thread
    total_spools_of_thread_price = total_spools_of_thread * thread_price_per_spool  # Total price of the two spools of silver thread

    # Calculate the total amount spent on the fabric, pattern and thread
    total_cost = pattern_price + total_spools_of_thread_price + velvet_price_per_yard * yards_of_fabric

    # Find the number of yards of fabric purchased
    yards_of_fabric = (total_cost - pattern_price - total_spools_of_thread_price) / velvet_price_per_yard
    result = yards_of_fabric
    return result

print(solution())