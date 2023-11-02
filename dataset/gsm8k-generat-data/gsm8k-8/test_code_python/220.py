def solution():
   # Calculate the miles per gallon for the car
   miles_per_gallon = 400 / 20

   # Calculate the amount of gas needed for a one-way trip
   gas_needed_for_one_way = 600 / miles_per_gallon

   # Calculate the total amount of gas needed for a round trip
   total_gas_needed = 2 * gas_needed_for_one_way

   # Calculate the additional amount of gas needed
   additional_gas_needed = total_gas_needed - 8

   result = additional_gas_needed
   return result

print(solution())