def solution():
    """Missy watches 5 28-minute reality shows and one 10-minute cartoon. How long does she spend watching TV?"""
    reality_shows = 5
    cartoon = 10
    reality_show_length = 28
    total_reality_show_length = reality_shows * reality_show_length
    total_time_spent = total_reality_show_length + cartoon
    result = total_time_spent
    return result

print(solution())