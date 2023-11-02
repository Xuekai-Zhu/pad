def solution():
    """The show Magic King was on the air for 10 seasons and 20 episodes per season for the first half of seasons and 25 for the second half of the show. How many total episodes were there?"""
    seasons = 10
    first_half_episodes = 20
    second_half_episodes = 25
    total_episodes = (first_half_episodes * (seasons // 2)) + (second_half_episodes * (seasons // 2))
    result = total_episodes
    return result

print(solution())