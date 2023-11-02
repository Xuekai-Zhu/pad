def solution():
    num_sections = 6
    collection_per_section = 280
    extra_collection = 320

    # Calculate the total collection after two weeks
    total_collection = num_sections * collection_per_section * 2

    # Calculate the target collection
    target_collection = total_collection + extra_collection

    result = target_collection
    return result

print(solution())