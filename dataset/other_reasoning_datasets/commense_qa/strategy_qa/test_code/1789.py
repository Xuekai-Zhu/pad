def solution():
    american_starbucks_menu = ["Lattes", "Cappucino"]
    chinese_starbucks_menu = ["Blackcurrant Raspberry Juiced Tea", "Iced Shaken Mango Herbal Juiced Tea", "Mooncakes"]
    familiar_items = []
    for item in american_starbucks_menu:
        if item in chinese_starbucks_menu:
            familiar_items.append(item)
    if familiar_items:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())