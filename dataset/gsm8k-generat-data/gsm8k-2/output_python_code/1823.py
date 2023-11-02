def solution():
    """Five food companies sponsored a local food bank. Foster Farms donated 45 dressed chickens; American Summits donated twice the number of bottled water than the number of dressed chicken donated by Foster Farms; Hormel donated three times the number of dressed chickens that Foster Farms donated; Boudin Butchers donated one-third of the number of dressed chickens that Hormel donated; Del Monte Foods donated 30 fewer bottles of water than American Summits. How many food items did the companies donate in total?"""
    foster_chickens = 45
    summit_water = foster_chickens * 2
    hormel_chickens = foster_chickens * 3
    boudin_chickens = hormel_chickens // 3
    delmonte_water = summit_water - 30
    total_items = foster_chickens + summit_water + hormel_chickens + boudin_chickens + delmonte_water
    result = total_items
    return result

print(solution())