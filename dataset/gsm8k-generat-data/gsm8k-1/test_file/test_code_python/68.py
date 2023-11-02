def solution():
    """Tommy is fundraising for his charity by selling brownies for $3 a slice and cheesecakes for $4 a slice. If Tommy sells 43 brownies and 23 slices of cheesecake, how much money does Tommy raise?"""
    brownie_price = 3
    cheesecake_price = 4
    brownie_slices = 43
    cheesecake_slices = 23
    total_brownie_sales = brownie_price * brownie_slices
    total_cheesecake_sales = cheesecake_price * cheesecake_slices
    total_sales = total_brownie_sales + total_cheesecake_sales
    result = total_sales
    return result

print(solution())