def solution():
    current_sale = 44000  # Porter made $44,000 from the recent painting
    previous_sale = (current_sale + 1000) / (5 * 1.0)  # $1000 less than 5 times the previous sale
    result = previous_sale
    return result

print(solution())