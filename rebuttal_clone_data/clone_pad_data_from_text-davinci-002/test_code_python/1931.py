minutes_in_an_hour = 60
    shop_hours = 10
    women_tshirt_frequency = 30
    men_tshirt_frequency = 40
    women_tshirt_price = 18
    men_tshirt_price = 15
    total_hours = shop_hours * 7
    total_women_tshirts_sold = total_hours * (1 / women_tshirt_frequency)
    total_men_tshirts_sold = total_hours * (1 / men_tshirt_frequency)
    total_tshirts_sold = total_women_tshirts_sold + total_men_tshirts_sold
    total_revenue = (total_women_tshirts_sold * women_tshirt_price) + (total_men_tshirts_sold * men_tshirt_price)
    result = total_revenue
    
    return result

print(solution())