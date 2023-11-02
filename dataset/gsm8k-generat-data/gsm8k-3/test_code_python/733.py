def solution():
    """Henry, John and Leo collected some seashells from the beach. Henry collected 11, Paul 24. If they initially collected 59 seashells in total and Leo gave a quarter of his collection to a younger kid they met, how many do they have in total now?"""
    # Define the number of seashells each person collected
    henry_shells = 11
    paul_shells = 24
    leo_shells = 59 - henry_shells - paul_shells

    # Calculate the number of seashells Leo gave away
    given_away = int(leo_shells / 4)

    # Calculate the total number of seashells they have now
    total_shells = henry_shells + paul_shells + leo_shells - given_away

    # Display the total number of seashells they have now
    result = total_shells
    return result

print(solution())