from operator import concat

def bisect(func, a, b):
    def f(x):
        f = eval(func)
        return f
    error = abs(b-a)
    while error > 0.000001:
        c = (b+a)/2
        # print("a", a)
        # print("b", b)
        # print("c", c)
        # print("f(a)", f(a))
        # print("f(b)", f(b))
        # print("f(c)", f(c))
        if f(c) * f(a) < 0:
            b = c
            error = abs(b-a)
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b-a)
        # elif f(c) > 0:
        #     a = (f(c))/2
        #     break
        else:
            print("no root")
            quit()
    return a

def sq_root(func):
    poly_eq1 = func.replace('-','')
    poly_eq1 = poly_eq1.replace(' + ','')
    poly_eq1 = poly_eq1.replace('*x**0', '')
    poly_eq1 = poly_eq1.replace('*x**1', '')
    poly_eq1 = poly_eq1.replace('*x**2', '')
    num_pol = int(poly_eq1)
    sq_root = int(num_pol**0.5)
    if (sq_root) % 1 == 0:
        return True
    return False

def solve(coefficients, interval):
    poly_eq = ''
    sq = ''
    z = True
    a, b = map(float, interval.split())
    for i, j in enumerate(coefficients):
            if j != 0:
                sq+=str(int(j))
                temp = concat(str(int(j)), '*x**')
                temp2 = concat(temp, str(i))
                res = concat(temp2, ' + ')
                poly_eq = concat(poly_eq, res)
    func = poly_eq[:-3]
    if sq_root(func):
        str_num = str(sq_root)
        return int(str_num[0]) / int(str_num[1])
    return bisect(func, a, b)
#-2 0 -1 0 1
#-5 5
# 4 -4 1
if __name__ == '__main__':
    done = False
    while not done:
        coefficients = list(map(float, input('Enter the polynomial coefficients:\n').split()))
        interval = input('Enter the interval:\n')
        root = solve(coefficients, interval)
        print(f'Root found at {root:.6f}.')
        answer = input('Do you want to continue? [Y/N]\n').upper()
        if answer != 'Y':
            done = True