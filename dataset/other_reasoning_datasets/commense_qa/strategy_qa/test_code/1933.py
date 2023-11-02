def solution():
    chlorine_prevents_algae_growth = True
    algae_photosynthesize = True
    if chlorine_prevents_algae_growth and algae_photosynthesize:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())