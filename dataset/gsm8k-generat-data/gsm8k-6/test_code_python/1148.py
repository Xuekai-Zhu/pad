def solution():
    # Calculate the number of grains of rice in half a cup
    rice_in_half_cup = 480 * 0.5
  
      # Convert half a cup to teaspoons and calculate the number of grains of rice in one teaspoon
    rice_in_one_teaspoon = (rice_in_half_cup / 8) / 3

    result = rice_in_one_teaspoon
    return result

print(solution())