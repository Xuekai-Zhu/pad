def solution():
     tshirt_price = 5
     pants_price = 4
     skirts_price = 6
     num_tshirts_sold = 2
     num_pants_sold = 1
     num_skirt_sold = 4
     num_refurb_tshirts_sold = 6
     refurb_tshirt_price = tshirt_price / 2
     
     total_price = (num_tshirts_sold * tshirt_price) + (num_pants_sold * pants_price) + (num_skirt_sold * skirts_price) + (num_refurb_tshirts_sold * refurb_tshirt_price)
     result = total_price
     return result

print(solution())