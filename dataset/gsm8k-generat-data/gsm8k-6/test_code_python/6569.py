def solution():
    # Calculate the total cost of the trip
    price_per_person = 147  
    discount_per_person = 14  
    total_discount = 2 * discount_per_person 
    total_price = 2 * price_per_person - total_discount  
    result = total_price
    return result

print(solution())