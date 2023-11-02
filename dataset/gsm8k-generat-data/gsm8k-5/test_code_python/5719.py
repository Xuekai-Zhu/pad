def solution():
    azure_valley_skirts = 60  # Given that Azure Valley has 60 skirts
    seafoam_valley_skirts = (2/3) * azure_valley_skirts  # Given that Seafoam Valley has two-thirds as many skirts as Azure Valley
    purple_valley_skirts = (1/4) * seafoam_valley_skirts  # Given that Purple Valley has one-quarter as many skirts as Seafoam Valley

    result = purple_valley_skirts
    return result

print(solution())