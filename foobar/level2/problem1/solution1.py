fib_cache = {}

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if fib_cache.get(n, 0):
        return fib_cache[n]
    result = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = result
    return result


def geometric_series(n):
    return 2 ** (n - 1)


def total_henchmen_count(total_lambs, mode, index=1, total_henchmen=0):
    nth_term = geometric_series(index) if mode == 'g' else fibonacci(index)
    if nth_term <= total_lambs:
        total_henchmen += 1
        index += 1
        total_lambs -= nth_term
        return total_henchmen_count(total_lambs, mode, index=index, total_henchmen=total_henchmen)
    else:
        return total_henchmen


def solution(total_lambs):
    generous = total_henchmen_count(total_lambs, 'g')
    stingy = total_henchmen_count(total_lambs, 's')
    return stingy - generous