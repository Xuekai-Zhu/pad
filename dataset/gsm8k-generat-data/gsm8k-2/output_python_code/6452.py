def solution():
    """Allie's making guacamole for a party. Each batch requires 4 avocados and serves about 6 people. If 42 people are going to be at the party including her, how many avocados does she need?"""
    batch_size = 4
    serving_size = 6
    total_people = 42
    batches_needed = total_people / serving_size
    avocados_needed = batches_needed * batch_size
    result = avocados_needed
    return result

print(solution())