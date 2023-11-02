def solution():
     mary_platter = 20
     mary_bread = 2
     elle_soda = 1.50 * 2
     andrea_soda = 1.50 * 2
     elle_chicken = 10
     andrea_chicken = 10
     joe_cake = 5
     others_total = elle_soda + andrea_soda + elle_chicken + andrea_chicken + joe_cake
     mary_total = mary_platter + mary_bread
     result = mary_total - others_total
     return result

print(solution())