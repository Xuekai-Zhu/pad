def solution():
    """Justin bought some jerseys. He bought four long-sleeved ones that cost $15 each, and some striped ones that cost $10 each. How many striped jerseys did Justin buy if he spent a total of $80?"""
    long_sleeve_price = 15
    striped_price = 10
    long_sleeve_quantity = 4
    total_spent = 80
    total_long_sleeve_cost = long_sleeve_price * long_sleeve_quantity
    striped_quantity = (total_spent - total_long_sleeve_cost) / striped_price
    result = striped_quantity
    return result

print(solution())