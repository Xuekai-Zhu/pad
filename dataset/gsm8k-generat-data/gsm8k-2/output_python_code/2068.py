def solution():
    """Page collects fancy shoes and has 80 pairs in her closet. She decides to donate 30% of her collection that she no longer wears. After dropping off her donation, she treats herself and buys 6 more pairs to add to her collection. How many shoes does she have now?"""
    original_shoe_count = 80
    donation_count = int(original_shoe_count * 0.3)
    remaining_count = original_shoe_count - donation_count
    new_count = remaining_count + 6
    result = new_count
    return result

print(solution())