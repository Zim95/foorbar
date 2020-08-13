'''
Assuming that the values come from standart input
'''

def answer(a, n):
    if not a:
        return []
    if n == 0:
        return []
    visited = {}
    for index, item in enumerate(a):
        if item in visited:
            visited[item]['count'] += 1
            visited[item]['index'].append(index)
        else:
            visited[item] = {}
            visited[item]['count'] = 1
            visited[item]['index'] = [index]
    
    deleted_count = 0
    for item, info in visited.items():
        count = info.get('count', 0)
        indexes = info.get('index', [])
        if count > n:
            for index in indexes:
                del a[index - deleted_count]
                deleted_count += 1
    return a


if __name__ == "__main__":
    a = list(map(int, input().split(" ")))
    n = int(input())
    print(answer(a, n))