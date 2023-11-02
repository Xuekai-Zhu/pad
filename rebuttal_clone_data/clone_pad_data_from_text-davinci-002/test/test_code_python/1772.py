def solution():
     buckets_needed = 110
     buckets_per_round_george = 2
     buckets_per_round_harry = 3
     rounds_needed = buckets_needed / (buckets_per_round_george + buckets_per_round_harry)
     result = rounds_needed
 
     return result

print(solution())