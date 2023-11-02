def solution():
     population_wellington = 900
     population_lazy_harbor = population_wellington - 800
     population_port_perry = population_lazy_harbor * 7
     population_combined = population_lazy_harbor + population_port_perry
     result = population_combined
     return result

print(solution())