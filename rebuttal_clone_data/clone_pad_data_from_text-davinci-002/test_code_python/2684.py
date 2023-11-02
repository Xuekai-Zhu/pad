def solution():
    ticket_price = 5
    deep_fried_food_price = 8
    ride_price = 4
    souvenir_price = 15
    total_ticket_sales = 2520
    total_sales = total_ticket_sales + (total_ticket_sales * 2/3 * deep_fried_food_price) + (total_ticket_sales * 1/4 * ride_price) + (total_ticket_sales * 1/8 * souvenir_price)
    result = total_sales
    return result

print(solution())