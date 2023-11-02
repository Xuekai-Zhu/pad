def solution():
    """Susie's pet lizard Moe takes 10 seconds to eat 40 pieces of cuttlebone each day. How long would it take Moe to eat 800 pieces?"""
    # Define the time it takes Moe to eat 40 cuttlebones
    TIME_PER_40_CUTTLEBONES = 10  # seconds

    # Calculate the ratio of cuttlebones to time
    cuttlebones_per_second = 40 / TIME_PER_40_CUTTLEBONES

    # Calculate the time it would take Moe to eat 800 cuttlebones
    time_to_eat_800 = 800 / cuttlebones_per_second

    # return the result in seconds
    result = time_to_eat_800
    return result

print(solution())