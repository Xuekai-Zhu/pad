def solution():
    current_release = "focal fossa"
    linux_distributions = ["Ubuntu", "Debian", "Fedora", "Arch Linux", "Mint", "CentOS"]
    if current_release in linux_distributions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())