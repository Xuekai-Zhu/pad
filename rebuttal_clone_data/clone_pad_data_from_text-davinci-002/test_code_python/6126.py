def solution():
    pencils_made = 100
    pencils_sold = 350
    pencils_in_stock = 80
    pencils_left = pencils_made - pencils_sold + pencils_in_stock
    result = pencils_left
    return result

print(solution())