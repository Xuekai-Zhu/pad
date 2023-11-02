def solution():
    """Lillian's garden doesn't have any bird feeders in it so she wants to add some. She builds 3 and buys 3 others. Each bird feeder seems to attract 20 birds throughout the day until Lillian notices that the birds seem to prefer the feeders she made herself which attract 10 more birds each than the store-bought ones.
    How many birds can Lillian expect to see in her garden each day if the same amount keep coming to her bird feeders?"""
    self_made_feeders = 3
    store_bought_feeders = 3
    birds_attracted_store_bought = 20
    additional_birds_attracted_self_made = 10
    total_birds_attracted = (
        self_made_feeders * (birds_attracted_store_bought + additional_birds_attracted_self_made)
        + store_bought_feeders * birds_attracted_store_bought
    )
    result = total_birds_attracted
    return result

print(solution())