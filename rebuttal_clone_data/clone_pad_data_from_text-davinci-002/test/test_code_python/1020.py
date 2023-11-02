def solution():
    guitar_price = 1000
    guitar_center_discount = 15
    guitar_center_shipping = 100
    sweetwater_discount = 10
    guitar_center_total = guitar_price - (guitar_price * (guitar_center_discount / 100)) + guitar_center_shipping
    sweetwater_total = guitar_price - (guitar_price * (sweetwater_discount / 100))
    cheaper_store = min(guitar_center_total, sweetwater_total)
    expensive_store = max(guitar_center_total, sweetwater_total)
    result = expensive_store - cheaper_store
    return result

print(solution())