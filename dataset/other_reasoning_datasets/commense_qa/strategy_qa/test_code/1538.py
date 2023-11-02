def solution():
    fiat_chrysler_car_brands = 10
    asian_car_brands = ["Toyota", "Honda", "Nissan", "Mazda", "Subaru"]
    japanese_cars_association = [brand for brand in asian_car_brands if brand in fiat_chrysler_car_brands]
    if japanese_cars_association:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())