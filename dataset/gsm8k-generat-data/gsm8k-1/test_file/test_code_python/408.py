def solution():
    """Shannon makes her own madeleine cookies and eats 2 a night as a treat. She wants to make enough cookies to last her for 30 days by storing them in the freezer. Her recipe makes 1 dozen madeleine cookies. How many dozens of cookies will she need to make so she has enough for 30 days?"""
    cookies_per_day = 2
    days = 30
    recipe_yield = 12
    cookies_needed = cookies_per_day * days
    dozens_needed = cookies_needed / recipe_yield
    result = dozens_needed
    
    return result

print(solution())