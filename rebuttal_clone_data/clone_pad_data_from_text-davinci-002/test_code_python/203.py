def solution():
     """Benny bought  2 soft drinks for$ 4 each and 5 candy bars. He spent a total of 28 dollars. How much did each candy bar cost?"""
     cost_of_drinks = 4 * 2
     cost_of_candy = 28 - cost_of_drinks
     cost_per_candy = cost_of_candy / 5
     result = cost_per_candy
     return result

print(solution())