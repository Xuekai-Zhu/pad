def solution():
    # Calculate the total number of pencils made during the week
    total_pencils_made = 100 * 5  # Paul makes 100 pencils a day five days a week

    # Calculate the number of pencils in stock at the end of the week
    pencils_in_stock = total_pencils_made + 80 - 350  # Paul started the week with 80 pencils in his stock and sold 350 pencils during the week
    result = pencils_in_stock
    return result

print(solution())