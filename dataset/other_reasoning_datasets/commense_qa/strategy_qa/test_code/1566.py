def solution():
    exclusive_patronage = False
    if "Leonardo Da Vinci" in ["Lorenzo de Medici"]:
        exclusive_patronage = True
    return "no" if exclusive_patronage else "yes"

print(solution())