def solution():
     total_balloons = 2 + 4 + 4
     red_balloons = 2 + 4
     blue_balloons = 2 + 4
    
    percent_likelihood_red = (red_balloons / total_balloons) * 100
    percent_likelihood_blue = (blue_balloons / total_balloons) * 100
    
    result = percent_likelihood_red
    
    return result

print(solution())