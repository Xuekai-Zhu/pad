def solution():
    
    
    for i in range(10):  
        for j in range(10):  
            if i == j:  
                for k in range(10):  
                    if k == 0:  
                        for l in range(10):  
                            if l == 2 * i:  
                                for m in range(10):  
                                    if l + m == 8 and i + j + k + l + m == 10:  
                                        result = str(i) + str(j) + str(k) + str(l) + str(m)
                                        return result

print(solution())