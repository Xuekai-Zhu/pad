def solution():
     total_strawberries = 300
     strawberries_per_bucket = total_strawberries / 5
     strawberries_taken_out = 20
     strawberries_left = strawberries_per_bucket - strawberries_taken_out
     result = strawberries_left
     return result

print(solution())