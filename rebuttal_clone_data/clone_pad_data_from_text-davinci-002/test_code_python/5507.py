def solution():
     bench_weight = 1000
     bench_safety_margin = 20
     max_weight = bench_weight - (bench_weight * (bench_safety_margin / 100))
     johns_weight = 250
     weight_allowed = max_weight - johns_weight
     result = weight_allowed
     return result

print(solution())