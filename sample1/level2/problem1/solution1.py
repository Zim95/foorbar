def solution(string):
    if not string:
        return 0
    if string.find(">") == -1:
        return 0
    if string.find("<") == -1:
        return 0
    sample = string.replace("-", "")[string.find(">"):]
    right_movers = ''
    total_encounters = 0
    for item in sample:
        if item == ">":
            right_movers += item
        elif item == "<":
            total_encounters += len(right_movers)
    return total_encounters * 2


if __name__ == "__main__":
    string = input()
    print(solution(string))