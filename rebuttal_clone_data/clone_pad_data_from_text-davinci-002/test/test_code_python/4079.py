def solution():
     nc_gas_price = 2
     va_gas_price = nc_gas_price + 1
     nc_gallons = 10
     va_gallons = 10
     nc_spent = nc_gallons * nc_gas_price
     va_spent = va_gallons * va_gas_price
     total_spent = nc_spent + va_spent
     
     return total_spent

print(solution())