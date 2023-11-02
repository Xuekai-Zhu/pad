def solution():
     tallest = 100
     second_tallest = tallest / 2
     third_tallest = second_tallest / 2
     fourth_tallest = third_tallest / 5
     total_height = tallest + second_tallest + third_tallest + fourth_tallest
     result = total_height
     return result

print(solution())