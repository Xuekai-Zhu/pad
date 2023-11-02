def solution():
    """Paul makes pencils, making 100 pencils a day five days a week. He started the week with 80 pencils in his stock, and during the week he sold 350 pencils. How many pencils did he have in his stock at the end of the week?"""
    pencils_per_day = 100
    days_per_week = 5
    starting_stock = 80
    pencils_sold = 350
    total_pencils_made = pencils_per_day * days_per_week
    ending_stock = starting_stock + total_pencils_made - pencils_sold
    result = ending_stock
    return result

print(solution())