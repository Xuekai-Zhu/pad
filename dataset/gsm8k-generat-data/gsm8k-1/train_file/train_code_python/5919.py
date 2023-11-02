def solution():
    """In a store, there are three types of cheese: white, swiss, and blue cheese. Each cheese is packaged, and there are 200 grams of cheese in each package. The package prices are $5 for white cheese, $6 for swiss cheese, and $8 for blue cheese. Miley needed to get some for her party, and she decided to buy 5 packs of swiss cheese, 600 grams of blue cheese, and one-third less white cheese. How much did she need to pay for all the cheese?"""
    weight_per_package = 200
    price_per_white = 5
    price_per_swiss = 6
    price_per_blue = 8
    swiss_packs = 5
    blue_grams = 600
    white_percent = 2 / 3
    white_grams = int(weight_per_package * white_percent)
    total_grams = (swiss_packs * weight_per_package) + blue_grams + white_grams
    total_cost = (swiss_packs * price_per_swiss) + ((blue_grams // weight_per_package) * price_per_blue) + ((white_grams // weight_per_package) * price_per_white)
    result = total_cost
    return result

print(solution())