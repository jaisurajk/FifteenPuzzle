def solve(a, b):
    return a

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