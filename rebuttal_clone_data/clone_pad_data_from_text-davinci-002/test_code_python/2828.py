def solution():
    peter_magnets = 18 * 2
    adam_magnets = 18
    result = peter_magnets
    return result
    
Question: In 1990, the U.S. government increased the tax rate on cigarettes from 16 cents to 20 cents per pack.  If the price of a pack of cigarettes is now $3.50, by what percent did the price increase?
Solution: 
def solution():
    old_tax = .16
    new_tax = .20
    old_price = 3.50
    new_price = old_price + old_price * new_tax
    percent_increase = (new_price - old_price) / old_price
    result = percent_increase
    return result

print(solution())