def solution():
     expensive_lens = 300
     discount = 20
     total_discount = expensive_lens * (discount / 100)
     cheaper_lens = 220
     savings = total_discount - cheaper_lens
     result = savings
     return result

print(solution())