import re


def replacer(lst):
    result = []
    for item in lst:
        if item == '-':
            result.append(-1)
        elif (item == '+') | (item == ''):
            result.append(+1)
        else:
            result.append(int(item))
    return result


def solve(eqn):
    left = re.search(r'(.*)=', eqn).group(0)
    right = re.search(r'=(.*)', eqn).group(0)[1:] + '='
    left_numbers = replacer(re.findall(r'([+,-]?[\d]+)[^x^\d]', left.strip()))
    left_x = replacer(re.findall(r'([+,-]?[\d]{0,})x', left.strip()))
    right_numbers = replacer(re.findall(r'([+,-]?[\d]+)[^x^\d]', right.strip()))
    right_x = replacer(re.findall(r'([+,-]?[\d]{0,})x', right.strip()))
    sum_numbers = sum(left_numbers) - sum(right_numbers)
    sum_x = sum(right_x) - sum(left_x)
    try:
        solution = sum_numbers / sum_x
    except ZeroDivisionError:
        solution = 'NO'
    return solution


if __name__ == '__main__':
    eqn = 'x=x'
    print(solve(eqn))