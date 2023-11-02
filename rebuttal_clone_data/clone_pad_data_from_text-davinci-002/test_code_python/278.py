def solution():
     """The price of a home is $98 per square foot (sq ft). The house is 2,400 sq ft and the barn out back is 1,000 sq ft. How much is this property?"""
     house_price = 98
     house_size = 2400
     barn_price = 98
     barn_size = 1000
     total_price = (house_price * house_size) + (barn_price * barn_size)
     result = total_price
     return result

print(solution())