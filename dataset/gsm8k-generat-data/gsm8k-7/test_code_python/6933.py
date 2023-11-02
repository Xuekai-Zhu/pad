def solution():
    lasagna_minced = 2 # in pounds
    cottage_pie_minced = 3 # in pounds
    total_minced = 500 # in pounds

    # Calculate the total minced meat used for lasagna
    lasagna_total_minced = 100 * lasagna_minced

    # Calculate the total minced meat used for cottage pie
    cottage_pie_total_minced = total_minced - lasagna_total_minced

    # Calculate the number of cottage pies made
    num_cottage_pies = cottage_pie_total_minced / cottage_pie_minced
    result = num_cottage_pies
    return result

print(solution())