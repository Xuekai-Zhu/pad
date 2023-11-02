def solution():
    """Daisy's Flower Shop sold 45 daisies on its first day. On their second day, they sold 20 more flowers than they did on their first day. On the third day, they sold 10 less than twice the flowers that were sold than on the second day. If the flower shop sold a total of 350 daisies for 4 days, how many daisies were sold on the 4th day?"""
    first_day_sales = 45
    second_day_sales = first_day_sales + 20
    third_day_sales = (2 * second_day_sales) - 10
    total_sales = 350
    fourth_day_sales = total_sales - (first_day_sales + second_day_sales + third_day_sales)
    result = fourth_day_sales
    return result

print(solution())