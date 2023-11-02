def solution():
    # Calculate the number of bracelets Zayne sold for $5 each
    sold_at_5 = 60 // 5  # Zayne made $60 from selling bracelets for $5 each
    
    # Calculate the number of bracelets Zayne sold for $8 for a pair
    sold_at_8 = (30 - sold_at_5) // 2
    
    # Calculate the total amount Zayne made from selling his bracelets
    total_sales = sold_at_5 * 5 + sold_at_8 * 4
    result = total_sales
    return result

print(solution())