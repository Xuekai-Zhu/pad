def solution():
     total_candy = 100
     candy_eaten = 8
     candy_ bowls = 4
     candy_self = 3
     candy_remaining = total_candy - candy_eaten - (candy_bowls * candy_self)
     result = candy_remaining / candy_bowls
     return result

print(solution())