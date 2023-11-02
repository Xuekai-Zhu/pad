def solution():
     number_of_cupcakes = 4 * 12
     cupcakes_given_away = 3
     total_cupcakes = number_of_cupcakes - cupcakes_given_away
     cousins = total_cupcakes / 3
     result = cousins
     return result

print(solution())