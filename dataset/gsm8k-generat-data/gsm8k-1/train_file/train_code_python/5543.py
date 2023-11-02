def solution():
    """An agricultural cooperative must ship 6500 kg of potatoes. During transport by truck, 150 kg are damaged and therefore cannot be sold. The potatoes are distributed in 50 kg bags, each bag being sold for $72. What will the sale of the potatoes bring?"""
    total_potatoes = 6500
    damaged_potatoes = 150
    usable_potatoes = total_potatoes - damaged_potatoes
    bags_of_potatoes = usable_potatoes // 50
    sale_price_per_bag = 72
    profit = bags_of_potatoes * sale_price_per_bag
    result = profit
    return result

print(solution())