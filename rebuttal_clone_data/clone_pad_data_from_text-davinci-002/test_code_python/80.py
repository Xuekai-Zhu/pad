def solution():
    """Jennifer purchased 40 cans of milk at the store before meeting her classmate Mark, who was also buying milk. Jennifer bought 6 additional cans for every 5 cans Mark bought. If Mark purchased 50 cans, how many cans of milk did Jennifer bring home from the store?"""
    cans_purchased_by_jennifer = 40
    cans_purchased_by_mark = 50
    cans_bought_per_5_cans_bought_by_mark = 6
    total_cans_purchased_by_jennifer = cans_purchased_by_jennifer + ((cans_purchased_by_mark / 5) * cans_bought_per_5_cans_bought_by_mark)
    result = total_cans_purchased_by_jennifer
    return result

print(solution())