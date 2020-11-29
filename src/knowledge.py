import numpy as np
import matplotlib.pyplot as plt

class Variable:
    def __init__(self, name):
        self.name = name
        self.values = {}
        self.domains = {}

    def add_value(self, value_name, member_func, dom):
        self.values[value_name] = member_func
        self.domains[value_name] = dom

    def plot(self, a, b):
        dom = np.linspace(a, b, 10000)
        fig, axs = plt.subplots(1,1)
        colors = ["r:", "b:", "g:"]
        c = 0
        for name, func in self.values.items():
            y = [func(i) for i in dom]
            axs.plot(dom, y, colors[c], label = name)
            c += 1
        axs.legend()
        plt.savefig(f'{self.name}.png')
        plt.show()
        

class Rule:
    def __init__(self, rule_str):
        self.str = rule_str
        self.antecedents = []
        self.consequent = None

    def add_antecedent(self, var_name, value, neg):
        self.antecedents.append((var_name, value, neg))

    def add_consequent(self, var_name, value):
        self.consequent = (var_name, value)

    def __str__(self):
        return self.str

def parse_rule(rule_str):
    parts = rule_str.split("=>")
    ant_clauses = parts[0].split("and")
    cons_clauses = parts[1]
   
    r = Rule(rule_str)
    for c in ant_clauses:
        var, value = c.split("is")
        var = var.split()
        value = value.split()
        if len(var) > 1:
            r.add_antecedent(var[1], value[0], True)
        else:
            r.add_antecedent(var[0], value[0], False)
    
    c_var, c_value = cons_clauses.split("is")
    c_var = c_var.split()[0]
    c_value = c_value.split()[0]
    r.add_consequent(c_var, c_value)
    return r


if __name__ == "__main__":
    r = " not A is a1 and B is b1 and C is c1 => D is d1"
    r = parse_rule(r, (0, 50))
    print(r)

    


