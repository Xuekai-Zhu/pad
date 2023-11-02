def solution():
    """At Penny’s bakery, her famous blueberry cheesecakes are $7 a slice. Each cheesecake pie is cut into 6 thick slices. If she sells 7 cheesecake pies, how much money does she make?"""
    slice_price = 7
    slices_per_pie = 6
    pies_sold = 7
    total_slices = pies_sold * slices_per_pie
    total_money = total_slices * slice_price
    result = total_money
    return result

print(solution())