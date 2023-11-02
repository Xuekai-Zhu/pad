def solution():
    total_money = 100
    heaven_sharpeners = 2
    heaven_notebooks = 4
    heaven_spending = (heaven_sharpeners * 5) + (heaven_notebooks * 5)
    brother_spending = total_money - heaven_spending
    brother_erasers = 10
    brother_eraser_price = 4
    brother_eraser_spending = brother_erasers * brother_eraser_price
    brother_highlighter_spending = brother_spending - brother_eraser_spending
    result = brother_highlighter_spending
    return result

print(solution())