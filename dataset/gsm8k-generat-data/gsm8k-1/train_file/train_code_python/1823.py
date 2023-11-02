def solution():
    """Five food companies sponsored a local food bank. Foster Farms donated 45 dressed chickens; American Summits donated twice the number of bottled water than the number of dressed chicken donated by Foster Farms; Hormel donated three times the number of dressed chickens that Foster Farms donated; Boudin Butchers donated one-third of the number of dressed chickens that Hormel donated; Del Monte Foods donated 30 fewer bottles of water than American Summits. How many food items did the companies donate in total?"""
    chickens_foster = 45
    water_american = chickens_foster * 2
    chickens_hormel = chickens_foster * 3
    chickens_boudin = chickens_hormel / 3
    water_delmonte = water_american - 30
    total_items = chickens_foster + water_american + chickens_hormel + chickens_boudin + water_delmonte
    result = total_items
    return result

print(solution())