import numpy as np
import matplotlib.pyplot as plt

class Variable:
    def __init__(self, name):
        self.name = name
        self.values = {}

    def add_value(self, value_name, member_func):
        self.values[value_name] = member_func

    def fuzzify(self):
        pass

    def plot(self, dom = np.linspace(0, 100, 10000) ):
        fig, axs = plt.subplots(1,1)
        colors = ["r:", "b:", "g:"]
        c = 0
        for name, func in self.values.items():
            y = [func(i) for i in dom]
            axs.plot(dom, y, colors[c], label = name)
            c += 1
        axs.legend()
        plt.show()
        

class Rule:
    def __init__(self):
        self.antecedents = []
        self.consequent = None

    def add_antecedent(self, var_name, value):
        self.antecedents.append((var_name, value))

    def add_consequent(self, var_name, value):
        self.consequent = (var_name, value)

