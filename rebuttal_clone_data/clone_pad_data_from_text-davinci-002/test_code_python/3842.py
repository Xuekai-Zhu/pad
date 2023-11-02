def solution():
     shirt_price = 0.75 * pants_price
     shoe_price = pants_price + 10
     total_price = shirt_price + pants_price + shoe_price
     return total_price - 340

print(solution())