def solution():
    """Page collects fancy shoes and has 80 pairs in her closet. She decides to donate 30% of her collection that she no longer wears. After dropping off her donation, she treats herself and buys 6 more pairs to add to her collection. How many shoes does she have now?"""
    initial_collection = 80
    donation_percent = 30
    donated_pairs = int(initial_collection * (donation_percent / 100))
    remaining_pairs = initial_collection - donated_pairs
    new_pairs = 6
    total_pairs = remaining_pairs + new_pairs
    result = total_pairs
    return result

print(solution())