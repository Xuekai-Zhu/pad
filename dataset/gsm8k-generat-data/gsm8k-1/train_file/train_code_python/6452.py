def solution():
    """Allie's making guacamole for a party. Each batch requires 4 avocados and serves about 6 people. If 42 people are going to be at the party including her, how many avocados does she need?"""
    people_per_batch = 6
    people_at_party = 42
    avocados_per_batch = 4
    batches_needed = (people_at_party - 1) // people_per_batch + 1
    avocados_needed = batches_needed * avocados_per_batch
    result = avocados_needed
    return result

print(solution())