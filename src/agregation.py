from membership import *

class Mamdani:
    def __init__(self, defuzzifier, op):
        """
        defuzzifier: defuzzifer method(bisector, centroid, mean_max, left_max, right_max)
        op: operator for fuzzificate each rule (min, max, product)
        """
        self.defuzzifier = defuzzifier
        self.op = op 

    def predict(self, variables, umbral_corts, rules):
        out_var_func = {} # {var_name: agregate_function}

        i = 0
        for r in rules:
            var_name, value = r.consequent
            dom = variables[var_name].domains[value]
            f = variables[var_name].values[value]
            c = corte(umbral_corts[i])
            f = intersection(f, c)

            if not out_var_func.__contains__(var_name):
                out_var_func[var_name] = (f, dom)
            else:
                last_f, last_dom = out_var_func[var_name]
                a, b = dom
                la, lb = last_dom
                na = min(a, la)
                nb = max(b, lb) 
                f = union(f, last_f )
                out_var_func[var_name] = (f, (na, nb))
            i += 1
            
        defuzzi_values = {}
        for var, value in out_var_func.items():
            f, dom = value
            a, b = dom
            plot_func(f)
            defuzzi_values[var] = self.defuzzifier(f, a, b)

        return defuzzi_values

class Larsen:
    def __init__(self, defuzzifier, op):
        """
        defuzzifier: defuzzifer method(bisector, centroid, mean_max, left_max, right_max)
        op: operator for fuzzificate each rule (min, max, product)
        """
        self.defuzzifier = defuzzifier
        self.op = op 

    def predict(self, variables, umbral_corts, rules):
        out_var_func = {} # {var_name: agregate_function}
        
        i = 0
        for r in rules:
            var_name, value = r.consequent
            dom = variables[var_name].domains[value]
            f = variables[var_name].values[value]
            f = scalar_mult(umbral_corts[i], f)
            if not out_var_func.__contains__(var_name):
                out_var_func[var_name] = (f, dom)
            else:
                last_f, last_dom = out_var_func[var_name]
                a, b = dom
                la, lb = last_dom
                na = min(a, la)
                nb = max(b, lb) 
                f = union(f, last_f )
                out_var_func[var_name] = (f, (na, nb))
            i += 1
            
        defuzzi_values = {}
        for var, value in out_var_func.items():
            f, dom = value
            a, b = dom
            plot_func(f)
            defuzzi_values[var] = self.defuzzifier(f, a, b)

        return defuzzi_values

        


        