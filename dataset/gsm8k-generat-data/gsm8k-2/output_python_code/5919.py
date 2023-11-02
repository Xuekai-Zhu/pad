def solution():
    """
    In a store, there are three types of cheese: white, swiss, and blue cheese. Each cheese is packaged,
    and there are 200 grams of cheese in each package. The package prices are $5 for white cheese,
    $6 for swiss cheese, and $8 for blue cheese. Miley needed to get some for her party,
    and she decided to buy 5 packs of swiss cheese, 600 grams of blue cheese,
    and one-third less white cheese. How much did she need to pay for all the cheese?
    """
    white_cheese_packs = (2/3) * 5
    total_white_cheese = white_cheese_packs * 200
    swiss_cheese_price = 6
    swiss_cheese_packs = 5
    total_swiss_cheese = swiss_cheese_packs * 200 * swiss_cheese_price
    blue_cheese_price = 8
    total_blue_cheese = 600 * blue_cheese_price
    total_cost = total_white_cheese * 5 + total_swiss_cheese + total_blue_cheese
    result = total_cost
    return result

print(solution())