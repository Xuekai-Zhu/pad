def solution():
    """Anne purchased a box of sweets that contains 15 packs, and each pack has 60 pieces. She kept two packs and gave the rest to her 10 friends equally. How many pieces of sweets did each of her friends receive?"""
    total_packs = 15
    pieces_per_pack = 60
    packs_kept = 2
    packs_given = total_packs - packs_kept
    friends = 10
    pieces_per_friend = (packs_given * pieces_per_pack) / friends
    result = pieces_per_friend
    
    return result

print(solution())