def solution():
    """At Allan's house, there is twice as much corn as cannolis. He has a total of 40 cannolis in his house.
    Allan bought 60 more cannolis at the store and 40 fewer corns than the number of cannolis.
    Find the combined total of the number of corns and cannolis Allan has in the house?"""
    cannolis_initial = 40
    corns_initial = 2 * cannolis_initial
    cannolis_bought = 60
    corns_bought = cannolis_initial - 40
    total_cannolis = cannolis_initial + cannolis_bought
    total_corns = corns_initial - corns_bought
    combined_total = total_cannolis + total_corns
    result = combined_total
    return result

print(solution())