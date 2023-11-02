def solution():
    """Susie's pet lizard Moe takes 10 seconds to eat 40 pieces of cuttlebone each day. How long would it take Moe to eat 800 pieces?"""
    pieces_per_day = 40
    time_per_day = 10
    pieces_to_eat = 800
    time_to_eat = (pieces_to_eat / pieces_per_day) * time_per_day
    result = time_to_eat
    return result

print(solution())