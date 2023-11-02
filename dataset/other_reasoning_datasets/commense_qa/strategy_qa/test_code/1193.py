def solution():
    lil_wayne_real_name = "Dwayne Michael Carter"
    jayz_real_name = "Shawn Corey Carter"
    lil_wayne_grammys = 5
    jayz_grammys = 22
    similar_real_name_grammys = lil_wayne_grammys * 4
    if similar_real_name_grammys > lil_wayne_grammys:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())