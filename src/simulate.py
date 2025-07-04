import numpy as np
import matplotlib.pyplot as plt

def plot_graph(formula, x_range=(-10, 10), resolution=1000):
    """
    Formula simulation using numpy and matplotlib for visualization.
    Example formulas: 'x^2', 'sin(x)', 'exp(x)', etc.
    
    Args:
    - formula (str): Formula to simulate, like 'x^2', 'sin(x)', etc.
    - x_range (tuple): Range of x values (default: -10 to 10)
    - resolution (int): Number of points for smooth curve (default: 1000)
    """
    x = np.linspace(x_range[0], x_range[1], resolution)
    
    # Handle formula evaluation
    if formula == 'x^2':
        y = x ** 2
    elif formula == 'sin(x)':
        y = np.sin(x)
    elif formula == 'exp(x)':
        y = np.exp(x)
    else:
        print(f"[x] Formula '{formula}' not supported!")
        return
    
    # Plotting the graph
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'Formula: {formula}')
    plt.title(f'Graph of {formula}')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("[📊] Choose the formula to simulate:")
    print("1. x^2")
    print("2. sin(x)")
    print("3. exp(x)")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        plot_graph('x^2')
    elif choice == '2':
        plot_graph('sin(x)')
    elif choice == '3':
        plot_graph('exp(x)')
    else:
        print("[x] Invalid choice!")
