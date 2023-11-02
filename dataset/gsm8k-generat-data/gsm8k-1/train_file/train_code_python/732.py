def solution():
    """Henry, John and Leo collected some seashells from the beach. Henry collected 11, Paul 24. If they initially collected 59 seashells in total and Leo gave a quarter of his collection to a younger kid they met, how many do they have in total now?"""
    henry_seashells = 11
    paul_seashells = 24
    initial_total = 59
    leo_seashells = initial_total - henry_seashells - paul_seashells
    leo_gives = leo_seashells / 4
    total_now = initial_total - leo_gives
    result = total_now
    return result

print(solution())