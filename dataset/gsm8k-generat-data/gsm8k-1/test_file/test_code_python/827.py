def solution():
    """An interior design firm offers installation for $129.00. It includes hanging 4 mirrors, 2 shelves, 1 chandelier, and 10 pictures. They will install additional items for an extra $15.00 per item. Angela has 6 mirrors and 2 chandeliers and 20 pictures that she needs installed/hung. How much will this cost her?"""
    base_price = 129
    extra_mirror_price = 15
    extra_chandelier_price = 15
    extra_picture_price = 15
    mirrors = 6
    chandeliers = 2
    pictures = 20
    total_price = (base_price 
                   + (mirrors - 4) * extra_mirror_price 
                   + (chandeliers - 1) * extra_chandelier_price 
                   + (pictures - 10) * extra_picture_price)
    result = total_price
    return result

print(solution())