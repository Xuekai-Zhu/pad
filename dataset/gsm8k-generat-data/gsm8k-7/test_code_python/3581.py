def solution():
    parts_cost = 3600
    patent_cost = 4500
    selling_price = 180

    # Calculate the total cost of creating the machine
    total_cost = parts_cost + patent_cost

    # Calculate the break-even quantity
    break_even_quantity = total_cost / (selling_price - (parts_cost / break_even_quantity))

    result = round(break_even_quantity)
    return result

print(solution())