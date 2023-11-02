def solution():
    """An agricultural cooperative must ship 6500 kg of potatoes. During transport by truck, 150 kg are damaged and therefore cannot be sold. The potatoes are distributed in 50 kg bags, each bag being sold for $72. What will the sale of the potatoes bring?"""
    total_potatoes = 6500
    damaged_potatoes = 150
    sellable_potatoes = total_potatoes - damaged_potatoes
    bag_size = 50
    bags_available = sellable_potatoes // bag_size
    bag_price = 72
    total_price = bags_available * bag_price
    result = total_price
    return result

print(solution())