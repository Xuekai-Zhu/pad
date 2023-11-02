def solution():
    """Paul makes pencils, making 100 pencils a day five days a week. He started the week with 80 pencils in his stock, and during the week he sold 350 pencils. How many pencils did he have in his stock at the end of the week?"""
    pencils_per_day = 100
    days_per_week = 5
    starting_pencils = 80
    total_pencils_made = pencils_per_day * days_per_week
    remaining_pencils = total_pencils_made + starting_pencils - 350
    result = remaining_pencils
    return result

print(solution())