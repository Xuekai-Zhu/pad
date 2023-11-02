def solution():
    initial_shoe_count = 80  # Page has 80 pairs of shoes in her closet
    shoes_donated = initial_shoe_count * 0.3  # Page donates 30% of her shoes
    shoes_remaining = initial_shoe_count - shoes_donated  # Page has this many shoes left after donating
    shoes_new = 6  # Page buys 6 new pairs of shoes
    shoes_total = shoes_remaining + shoes_new  # Page has this many shoes in total now
    result = shoes_total
    return result

print(solution())