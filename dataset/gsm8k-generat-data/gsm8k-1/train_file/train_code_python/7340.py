def solution():
    """LaKeisha is mowing lawns to raise money for a collector set of books. She charges $.10 for every square foot of lawn. The book set costs $150. If she has already mowed three 20 x 15 foot lawns, how many more square feet does she have to mow to earn enough for the book set?"""
    cost_of_book_set = 150
    area_mowed = (20 * 15) * 3
    cost_earned = area_mowed * 0.10
    remaining_area = (cost_of_book_set - cost_earned) / 0.10
    result = remaining_area
    return result

print(solution())