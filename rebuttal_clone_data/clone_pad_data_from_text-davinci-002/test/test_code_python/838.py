def solution():
     bags_of_jerky = 20
     customer_order = 60
     bags_per_batch = 10
     batches_needed = (customer_order - bags_of_jerky) / bags_per_batch
     days_needed = batches_needed * 1
     result = days_needed
     return result

print(solution())