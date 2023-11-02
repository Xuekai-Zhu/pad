def solution():
    go_origin = "Zhou dynasty"
    go_origin_date = "1046 BC – 256 BC"
    jia_sidao_period = "late Song dynasty"
    jia_sidao_period_date = "960 AD – 1279 AD"
    if go_origin_date < jia_sidao_period_date:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())