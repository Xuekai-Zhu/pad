def solution():
    bouquets_sold_monday = 12
    bouquets_sold_tuesday = bouquets_sold_monday * 3
    bouquets_sold_wednesday = bouquets_sold_tuesday / 3
    total_bouquets_sold = bouquets_sold_monday + bouquets_sold_tuesday + bouquets_sold_wednesday
    result = total_bouquets_sold
    return result

print(solution())