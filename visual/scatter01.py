import numpy as np
import matplotlib.pyplot as plt


def main():

    x1 = np.random.rand(100)*0.5
    y1 = np.random.rand(100)

    x2 = np.random.rand(100) * 0.5 + 0.5
    y2 = np.random.rand(100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(x1, y1, c="red", label="group1")
    ax.scatter(x2, y2, c="blue", label="group2")
    ax.set_title('first scatter plot')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(loc='upper left')

    plt.savefig("Py.png")


if __name__ == '__main__':
    main()
