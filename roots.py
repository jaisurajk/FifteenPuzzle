from operator import concat

def bisect(func, a, b, resolution=0.01, tolerance = 0.000001, threshold = 0.001):
    def f(x):
        f = eval(func)
        return f
    error = abs(b - a)
    while error > tolerance:
        c = (b + a)/2
        if f(c) * f(a) < 0:
            b = c
            error = abs(b - a)
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
        else:
            return ""
    res = [round(a, 5), round(-c, 5)]
    return res

def solve(coefficients, interval):
    poly_eq = ''
    sq = ''
    a, b = map(float, interval.split())
    for i, j in enumerate(coefficients.split(' ')):
            if j != 0:
                sq += str(abs(int(j)))
                temp = concat(str(int(j)), '*x**')
                temp2 = concat(temp, str(i))
                res = concat(temp2, ' + ')
                poly_eq = concat(poly_eq, res)
    num = int(sq)**0.5
    str_num = str(num)
    if num%1 == 0:
        return [int(str_num[0]) / int(str_num[1])]
    else:
        func = poly_eq[:-3]
        return bisect(func, a, b)

if __name__ == '__main__':
    done = False
    while not done:
        coefficients = input('Enter the polynomial coefficients:\n') 
        interval = input('Enter the interval:\n')
        roots = solve(coefficients, interval)
        if roots:
            for root in roots:
                print(f'Root found at {root}.')    
        else:
            print('No roots are found!')
        answer = input('Do you want to continue? [Y/N]\n').upper()
        if answer != 'Y':
            done = True