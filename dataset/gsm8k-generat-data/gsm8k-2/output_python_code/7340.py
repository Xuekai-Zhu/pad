def solution():
    """LaKeisha is mowing lawns to raise money for a collector set of books. She charges $.10 for every square foot of lawn. The book set costs $150. If she has already mowed three 20 x 15 foot lawns, how many more square feet does she have to mow to earn enough for the book set?"""
    price_per_square_foot = 0.1
    book_set_cost = 150
    total_area_mowed = (20*15)*3
    money_earned = price_per_square_foot * total_area_mowed
    remaining_area = (book_set_cost - money_earned) / price_per_square_foot
    result = remaining_area
    return result

print(solution())