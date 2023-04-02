def bisect(f, a, b):
    roots = []
    ranges = [(a, b)]
    while ranges:
        a, b = ranges.pop()
        c = (a + b) / 2
        while abs(a - b) >= 0.01:
            c = (a + b) / 2
            if abs(f(c)) < 0.001:
                f_roc = lambda x: sum(j*(i + 1) * x ** i for i, j in enumerate(f[1:]))
                print(roots + bisect(f_roc, a, b))
                break
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        if abs(a - b) >= 0.01:
            ranges.append((a, c))
            ranges.append((c, b))
        else:
            for i in [a, b]:
                if f(i) < 0.001:
                    roots.append(i)
    return roots

def solve(coefficients, interval):
    a, b = map(float, interval.split())
    return bisect(coefficients, a, b)

if __name__ == '__main__':
    done = False
    while not done:
        coefficients = list(map(float, input('Enter the polynomial coefficients:\n').split()))
        interval = input('Enter the interval (e.g. "-1, 1"):\n')
        roots = solve(coefficients, interval)
        if roots:
            for root in roots:
                print(f'Root found at {root:.6f}.')
        else:
            print('No roots are found!')
        answer = input('Do you want to continue? [Y/N]\n').upper()
        if answer != 'Y':
            done = True



