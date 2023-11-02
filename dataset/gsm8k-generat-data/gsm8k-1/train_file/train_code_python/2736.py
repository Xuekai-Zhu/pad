def solution():
    """On Monday a group of 7 children and 5 adults went to the zoo. On Tuesday a group of 4 children and 2 adults went as well. Child tickets cost $3, and adult tickets cost $4. How much money did the zoo make in total for both days?"""
    monday_children = 7
    monday_adults = 5
    tuesday_children = 4
    tuesday_adults = 2
    child_price = 3
    adult_price = 4
    monday_revenue = (monday_children * child_price) + (monday_adults * adult_price)
    tuesday_revenue = (tuesday_children * child_price) + (tuesday_adults * adult_price)
    total_revenue = monday_revenue + tuesday_revenue
    result = total_revenue
    return result

print(solution())