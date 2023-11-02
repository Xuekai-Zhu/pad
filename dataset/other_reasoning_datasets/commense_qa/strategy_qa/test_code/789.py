def solution():
    developing_countries = ["Afghanistan", "Bangladesh", "Bhutan", "Cambodia", "Kiribati", "Laos", "Myanmar", "Nepal", "Samoa", "Solomon Islands", "Tuvalu"]
    largest_exporter = "unknown"
    # Check if the United States is a developing country
    if "United States" not in developing_countries:
        largest_exporter = "no, the largest exporter is unknown"
    return largest_exporter

print(solution())