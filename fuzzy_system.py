from membership import complement

class FuzzySystem:
    def __init__(self, agregation_method):
        self.variables = {}
        self.rules = []
        self.agregation_method = agregation_method

    def add_variable(self, variable):
        self.variables[variable.name] = variable
    
    def add_rule(self, rule):
        self.rules.append(rule)

    def fuzzification(self, input_var_values):
        """
            input_var_values: dict {var_name: var_value}
            return: 
        """
        umbrals = []
        
        for r in self.rules:
            u = 1
            for c in r.antecedents:
                name, value, neg = c
                input_value = input_var_values[name]
                if neg: #if the clause is the type not A is a1
                    f = self.variables[name].values[value]
                    alpha = complement(f)(input_value)
                else:
                    alpha = self.variables[name].values[value](input_value)
                u = self.agregation_method.op(u, alpha)
                print(name, value, input_value, u)
            umbrals.append(u)
        return umbrals

    def inference(self, input_var_values):
        """
            input_var_values: dict {var_name: var_value}
        """
        umbral_corts = self.fuzzification(input_var_values)
        predict_dict = self.agregation_method.predict(self.variables, umbral_corts, self.rules)
        for var_name, predict_value in predict_dict.items():
            print(var_name, round(predict_value, 4))

if __name__ == "__main__":
    fuzzy = FuzzySystem()
