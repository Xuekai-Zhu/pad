def solution():
    
    collection_days = 3
    collection_amount = 200
    weeks_without_collection = 2
    first_week_amount = collection_days * collection_amount
    second_week_amount = (collection_days * collection_amount) / 2
    total_garbage = first_week_amount + second_week_amount
    
    return total_garbage

print(solution())