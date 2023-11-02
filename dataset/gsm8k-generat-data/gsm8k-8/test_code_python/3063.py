def solution():
    # Let's call the ages of the coworkers R, P, T, Ro, and Mi respectively
    # Roger's statement:
    # R = P + T + Ro + Mi
    # R + 50 = 2R + P + T + Ro + Mi (When Roger retires, his experience will be twice the others combined)
    
    # Peter's statement:
    # P - 7 = daughter's age when he joined
    # P + 12 = 19 (Now daughter is 19, so P is 7 years older than 19-12=7)
    # P = 19 - 12 + 7 = 14 (Peter is 14 years older than his daughter)
    
    # Tom's statement:
    # T = 2 * Ro
    
    # Robert's statement:
    # R - 4 = P
    # R = Mi + 2
    # Mi + 6 = P + T + Ro + Mi (Combined statement with Roger's statement)
    
    # Substituting Peter's and Tom's statements in Roger's statement:
    # R = 14 + Ro + 2 * Ro + (0.5 * R - 7) + (R - 2)
    # R = 3.5 * R + 15 * Ro - 35
    # R - 3.5 * R = -15 * Ro + 35
    # -2.5 * R = -15 * Ro + 35
    # R = 6Ro - 14
    
    # Substituting Robert's statement in the combined statement with Roger's statement:
    # Mi + 6 = R - 4 + 2Ro
    # Mi + 10 = 6Ro
    
    # Substituting the above value of Mi in the Roger's statement:
    # R = 14 + Ro + 2 * Ro + (0.5 * R - 7) + (6Ro - 10)
    # R = 4.5 * R + 21 * Ro - 32
    # R - 4.5 * R = -21 * Ro + 32
    # -2.5 * R = -21 * Ro + 32
    # R = 8.4Ro - 12.8
    
    # Equating the two expressions of R:
    # 6Ro - 14 = 8.4Ro - 12.8
    # 2.4Ro = 1.2
    # Ro = 0.5
    
    # Therefore, Roger has to work for:
    # 50 - (0.5+14+2*0.5+6*0.5-10) = 50 - 15.5 = 34.5 years
    result = 34.5
    return result

print(solution())