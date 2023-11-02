def solution():
    grandmother_dolls = 50  # Their grandmother has 50 dolls
    sister_dolls = grandmother_dolls + 2  # Rene's sister has 2 more dolls than their grandmother
    rene_dolls = 3 * sister_dolls  # Rene has three times as many dolls as her sister
    total_dolls = grandmother_dolls + sister_dolls + rene_dolls  # Calculate the total number of dolls
    result = total_dolls
    return result

print(solution())