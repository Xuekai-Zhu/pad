def solution():
    """A farmer harvested 250 potatoes. He bundled them in twenty-five's and sold each bundle for $1.90. He also harvested 320 carrots and bundled them in twenty's and sold each bundle for $2. If the farmer sold all his harvested crops, how much did he get in all?"""
    potato_count = 250
    potato_bundle_size = 25
    potato_bundle_price = 1.90
    potato_bundle_count = potato_count // potato_bundle_size
    potato_total_price = potato_bundle_count * potato_bundle_price

    carrot_count = 320
    carrot_bundle_size = 20
    carrot_bundle_price = 2
    carrot_bundle_count = carrot_count // carrot_bundle_size
    carrot_total_price = carrot_bundle_count * carrot_bundle_price

    total_earnings = potato_total_price + carrot_total_price
    result = total_earnings
    return result

print(solution())