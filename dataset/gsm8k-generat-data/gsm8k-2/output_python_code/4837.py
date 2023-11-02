def solution():
    """Six Grade 4 sections launched a recycling drive where they collect old newspapers to recycle. Each section collected 280 kilos in two weeks. After the third week, they found that they need 320 kilos more to reach their target. How many kilos of the newspaper is their target?"""
    sections = 6
    collection_per_section = 280
    total_collection = sections * collection_per_section
    additional_collection_needed = 320
    target_collection = total_collection + additional_collection_needed
    result = target_collection
    return result

print(solution())