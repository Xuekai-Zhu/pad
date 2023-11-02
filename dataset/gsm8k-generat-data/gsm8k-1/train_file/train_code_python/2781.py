def solution():
    """Susie's pet lizard Moe takes 10 seconds to eat 40 pieces of cuttlebone each day. How long would it take Moe to eat 800 pieces?"""
    time_per_40_pieces = 10
    pieces_to_eat = 800
    time_to_eat_all = (time_per_40_pieces / 40) * pieces_to_eat
    result = time_to_eat_all
    return result

print(solution())