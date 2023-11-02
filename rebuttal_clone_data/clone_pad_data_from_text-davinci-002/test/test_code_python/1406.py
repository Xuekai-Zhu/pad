def solution():
     shirts_sold = 4
     dresses_sold = 7
     shirt_price = 5
     total_revenue = 69
     dress_price = (total_revenue - (shirts_sold * shirt_price)) / dresses_sold
     result = dress_price
     return result

print(solution())