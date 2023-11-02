def solution():
    copies_sold_wednesday = 15
    copies_sold_thursday = 3 * copies_sold_wednesday
    copies_sold_friday = copies_sold_thursday / 5
    total_copies_sold = copies_sold_wednesday + copies_sold_thursday + copies_sold_friday
    result = total_copies_sold
    return result

print(solution())