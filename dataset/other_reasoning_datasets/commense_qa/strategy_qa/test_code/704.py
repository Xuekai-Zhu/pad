def solution():
    b52_cost = 60_000_000
    acdc_album_sales = 200_000_000
    lil_wayne_album_sales = 120_000_000
    acdc_bombers = acdc_album_sales // b52_cost
    lil_wayne_bombers = lil_wayne_album_sales // b52_cost
    if acdc_bombers > lil_wayne_bombers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())