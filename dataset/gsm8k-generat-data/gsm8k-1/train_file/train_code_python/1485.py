def solution():
    """Tammy just got her hair cut. For every 14 haircuts, she gets a free additional haircut. She has gotten 5 free haircuts already. She is 5 haircuts away from another free one. How many haircuts has she gotten there?"""
    haircuts_before_free = 14
    free_haircuts_received = 5
    haircuts_until_next_free = 5
    total_haircuts = (haircuts_before_free * free_haircuts_received) + haircuts_until_next_free
    result = total_haircuts
    return result

print(solution())