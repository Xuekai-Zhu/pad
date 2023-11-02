def solution():
    increase_percentage = 25  # The collection increased by 25%
    new_additions = 2  # Ethyl bought two new dolls for Lucy's collection
    original_collection = (new_additions / (increase_percentage / 100)) * 100  # Calculate the original collection before the addition
    total_collection = original_collection + new_additions  # Calculate the total collection after the addition
    result = total_collection
    return result

print(solution())