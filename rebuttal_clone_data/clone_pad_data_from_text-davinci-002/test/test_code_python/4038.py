def solution():
     geckos = 5
     gecko_insects = 6
     lizards = 3
     lizard_insects = gecko_insects * 2
     total_insects = (geckos * gecko_insects) + (lizards * lizard_insects)
     result = total_insects
     return result

print(solution())