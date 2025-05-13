from itertools import zip_longest
import matplotlib.pyplot as plt

CORRELATION_TYPE_AUTO = 1
CORRELATION_TYPE_CROSS = 2

class Correlation:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else a.copy()

    def compute(self, N):
        correlation_results = []
        for i in range(N):
            # Обчислення кореляції як сума добутків елементів
            c = [x1 * x2 for x1, x2 in zip_longest(self.a, self.b, fillvalue=0)]
            correlation_results.append(sum(c))
            # Зміщення масиву b
            self.b = [self.b[-1]] + self.b[:-1]  # Крок зміщення
        return correlation_results

    def auto_correlation(self, N):
        return self.compute(N)

    def cross_correlation(self, N):
        # Доповнюємо b нулями, якщо довжина a більша за довжину b
        if len(self.a) > len(self.b):
            self.b.extend([0] * (len(self.a) - len(self.b)))
        return self.compute(N)


def plot1(y):
    x = [i for i in range(len(y))]
    plt.bar(x, y, width=0.2)
    plt.show()


def get_input(prompt):
    while True:
        try:
            return list(map(float, filter(None, input(prompt).split(' '))))
        except ValueError:
            print("Введено некоректні дані, спробуйте знову.")


if __name__ == '__main__':
    X = get_input('x1[n] = ')
    correlation_type = int(input('auto_cor - 1 || cor - 2 :'))

    if correlation_type == CORRELATION_TYPE_AUTO:
        corr = Correlation(X)
        plot1(corr.auto_correlation(len(X)))
    else:
        Y = get_input('x2[n] = ')
        lenx = len(X)
        Y.extend([0] * (len(X) - len(Y)))  # доповнюємо Y до довжини X
        corr = Correlation(X, Y)
        plot1(corr.cross_correlation(len(X)))
