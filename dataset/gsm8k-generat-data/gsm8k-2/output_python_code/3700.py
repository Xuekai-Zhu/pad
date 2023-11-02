def solution():
    """John has a sneezing fit for 2 minutes. He sneezes once every 3 seconds. How many times does he sneeze?"""
    fit_duration = 120  # in seconds
    sneeze_interval = 3  # in seconds
    sneeze_count = fit_duration // sneeze_interval
    result = sneeze_count
    return result

print(solution())