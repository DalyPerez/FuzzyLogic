from membership import *


class Mamdani:
    def __init__(self, defuzzifier):
        self.defuzzifier = defuzzifier

    def predict(self, variables, umbral_corts, rules):
        out_var_func = {} # {var_name: agregate_function}
        print("umbrals:", umbral_corts)
        
        i = 0
        for r in rules:
            var_name, value = r.consequent
            f = variables[var_name].values[value]
            c = corte(umbral_corts[i])
            f = intersection(f, c)
            plot_func(f)
            if not out_var_func.__contains__(var_name):
                out_var_func[var_name] = f
            else:
                out_var_func[var_name] = union(f, out_var_func[var_name] )
            
            plot_func(out_var_func[var_name])
            i += 1
            
        
        # defuzzi_values = {}
        # for var, f in out_var_func.items():
        #     defuzzi_values[var] = self.defuzzifier(f)

        # return defuzzi_values
        


        