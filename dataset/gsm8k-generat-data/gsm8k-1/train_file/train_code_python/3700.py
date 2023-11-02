def solution():
    """John has a sneezing fit for 2 minutes. He sneezes once every 3 seconds. How many times does he sneeze?"""
    sneezing_fit_duration = 120 # seconds
    time_between_sneezes = 3 # seconds
    sneezes_per_minute = 60 / time_between_sneezes
    total_sneezes = sneezing_fit_duration // time_between_sneezes * sneezes_per_minute
    result = total_sneezes
    return result

print(solution())