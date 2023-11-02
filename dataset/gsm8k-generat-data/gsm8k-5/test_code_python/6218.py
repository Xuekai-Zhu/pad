def solution():
    lollipop_cost = 2  # Each lollipop costs $2
    pack_of_chocolate_cost = 4 * lollipop_cost  # A pack of chocolate costs the same as 4 lollipops
    total_cost = (4 * lollipop_cost) + (6 * pack_of_chocolate_cost)  # Blake bought 4 lollipops and 6 packs of chocolate
    total_paid = 6 * 10  # Blake gave the cashier 6 $10 bills
    change = total_paid - total_cost  # Calculate the change Blake will get back
    result = change
    return result

print(solution())