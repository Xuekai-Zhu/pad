def solution():
    # Calculate the total amount donated by the customers
    total_donated = 3 * 40  # average customer donates 3 and there are 40 customers
    
    # Calculate the amount donated by the restaurant
    donated_by_restaurant = (total_donated // 10) * 2  # restaurant donates $2 for every $10 donated
    
    result = donated_by_restaurant
    return result

print(solution())