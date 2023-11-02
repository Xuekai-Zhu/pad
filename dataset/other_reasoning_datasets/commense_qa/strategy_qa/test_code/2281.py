def solution():
    pan_domains = ["wild", "shepherds", "flocks"]
    boy_who_cried_wolf_job = "shepherd"
    if boy_who_cried_wolf_job in pan_domains:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())