def solution():
    """The garbage truck passes through Daniel's neighborhood on Tuesdays, Thursdays, and Saturdays. In each garbage collection, an average of 200 kg is taken. Due to obstruction in the roads leading to Daniel's neighborhood, the garbage truck stops passing through for two weeks. During the first week, people in Daniel's neighborhood pile the extra garbage around the dumpster, during the second week they apply a policy of cutting their amount of garbage in half. How many kilograms of garbage have accumulated in Daniel's neighborhood during the 2 weeks?"""
    collection_days = 3
    collection_amount = 200
    weeks_without_collection = 2
    first_week_amount = collection_days * collection_amount
    second_week_amount = (collection_days * collection_amount) / 2
    total_garbage = first_week_amount + second_week_amount
    
    return total_garbage

print(solution())