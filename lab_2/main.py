from itertools import zip_longest
import matplotlib.pyplot as plt

def correlation1(a, b, N):
    d = []
    for i in range(N):
        c = [x1 * x2 for x1, x2 in zip_longest(a, b, fillvalue=0)]
        c = sum(c)
        d.append(c)
        b.append(b[0])
        del b[0]
    print('Answer : ', d, ' or ', end=' ')
    for x in d:
        print(round(x / N, 2), end=' ')
    return d

def auto_cor(a):
    b = a.copy()
    print('Auto Correlation')
    return correlation1(a, b, len(a))

def cor(a, b):
    print('Correlation')
    return correlation1(a, b, len(a))

def plot1(y):
    x = [i for i in range(len(y))]
    plt.bar(x, y, width=0.2)
    plt.show()

if __name__ == '__main__':
    # Очищення введених даних від зайвих пробілів або порожніх елементів
    X = list(map(float, filter(None, input('x1[n] = ').split(' '))))
    a = int(input('auto_cor - 1 || cor - 2 :'))
    
    if a == 1:
        # Auto-correlation
        plot1(auto_cor(X))
    else:
        # Cross-correlation
        Y = list(map(float, filter(None, input('x2[n] = ').split(' '))))
        # Make sure that both X and Y have the same length
        lenx = len(X)
        for i in range(len(Y) - lenx):
            Y.append(0)  # Adding zeros to Y if it's shorter than X
        plot1(cor(X, Y))
