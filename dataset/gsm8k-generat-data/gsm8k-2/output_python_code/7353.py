def solution():
    """Helen cuts her lawn starting in March and finishes in October. Her lawn mower uses 2 gallons of gas every 4th time she cuts her lawn. For March, April, September and October, she only cuts her law 2 times per month. In May, June, July and August, she has to cut her lawn 4 times per month. How many gallons of gas will she need to cut her lawn from March through October?"""
    gallons_per_cut = 0
    total_cuts = 0
    for month in ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']:
        if month in ['March', 'April', 'September', 'October']:
            cuts_per_month = 2
        else:
            cuts_per_month = 4

        total_cuts += cuts_per_month

        if total_cuts % 4 == 0:
            gallons_per_cut = 2

    total_gallons = gallons_per_cut * total_cuts
    result = total_gallons
    return result

print(solution())