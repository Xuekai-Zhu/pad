def solution():
    """Uriah's book bag is getting too heavy for him. He needs to remove 15 pounds from it. His comic books weigh 1/4 pound each and his toys weigh 1/2 pound each. If he removes 30 comic books, how many toys does he need to remove?"""
    weight_to_remove = 15
    comic_book_weight = 0.25
    toy_weight = 0.5
    comics_removed = 30
    total_weight_removed = comics_removed * comic_book_weight
    remaining_weight = weight_to_remove - total_weight_removed
    toys_to_remove = remaining_weight / toy_weight
    result = toys_to_remove
    return result

print(solution())