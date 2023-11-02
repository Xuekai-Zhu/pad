def solution():
     screens_sold_in_february = 8800 / 4
     screens_sold_in_march = 8800
     screens_sold_in_january = screens_sold_in_february / 2
     total_screens_sold = screens_sold_in_january + screens_sold_in_february + screens_sold_in_march
     result = total_screens_sold
     return result

print(solution())