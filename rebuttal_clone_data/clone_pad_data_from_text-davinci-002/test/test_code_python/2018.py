def solution():
    produce_mangoes = 400
    produce_apples = produce_mangoes * 2
    produce_oranges = produce_mangoes + 200
    total_produce = produce_mangoes + produce_apples + produce_oranges
    selling_price = 50
    total_revenue = selling_price * total_produce
    result = total_revenue
    return result

print(solution())