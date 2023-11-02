def solution():
    """At Penny's bakery, her famous blueberry cheesecakes are $7 a slice. Each cheesecake pie is cut into 6 thick slices. If she sells 7 cheesecake pies, how much money does she make?"""
    cheesecake_slices = 6
    cheesecake_price = 7 * cheesecake_slices
    total_pies = 7
    total_slices = cheesecake_slices * total_pies
    total_price = cheesecake_price * total_pies
    result = total_price
    return result

print(solution())