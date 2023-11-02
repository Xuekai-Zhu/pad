def solution():
    """Henry, John and Leo collected some seashells from the beach. Henry collected 11, Paul 24. If they initially collected 59 seashells in total and Leo gave a quarter of his collection to a younger kid they met, how many do they have in total now?"""
    # Define the initial number of seashells collected by Henry and Paul
    henry_seashells = 11
    paul_seashells = 24

    # Calculate the initial number of seashells collected by Leo
    total_seashells = 59
    leo_seashells = total_seashells - henry_seashells - paul_seashells

    # Calculate the number of seashells Leo gave away
    leo_gave_away = leo_seashells // 4

    # Calculate the total number of seashells after Leo gave some away
    total_seashells_now = total_seashells - leo_gave_away

    result = total_seashells_now
    return result

print(solution())