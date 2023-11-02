def solution():
    """A shoe store was having a weekend sale on a brand of popular tennis shoes. On Friday the store sold 14 pairs of tennis shoes. The next day they sold double that number of shoes. On the last day of the sale they sold one-half the amount that they did the day before, but six people returned their pairs because they didn't fit. How many tennis shoes were sold by the end of the sale?"""
    friday_sales = 14
    saturday_sales = friday_sales * 2
    sunday_sales = saturday_sales / 2 - 6
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())