def solution():
    # Let's assume there are 'x' adults attending the concert
    x = 1
    # The number of children attending the concert will be 3 times that of adults
    y = 3*x

    # The total revenue collected from adults' tickets will be 7*x
    revenue_adults = 7*x

    # The total revenue collected from children's tickets will be 3*y
    revenue_children = 3*y

    # The total revenue collected from all tickets will be $6,000
    total_revenue = 6000

    # The equation for total revenue
    # total_revenue = revenue_adults + revenue_children
    # Substitute the values and solve for 'x'
    x = (total_revenue - revenue_children) / (7 - 3)

    # The total number of people who bought tickets
    total_people = x + y
    result = total_people
    return result

print(solution())