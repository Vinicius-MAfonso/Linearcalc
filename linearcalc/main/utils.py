import re
import copy
class Exercise:
    def __init__(self, equations):
        variables_pattern = r"[a-zA-Z][\d]*"
        indepedent_terms_pattern = r"(?<=\=)(\s*(-?\d+\.?\d*)\s*)+$"
        before_equals_pattern = r"^.*?(?==)"
        coefficients_pattern = r'(([-]?\s*\d+\.?\d*)?(\s*[a-zA-Z]))'

        self.variables = re.findall(variables_pattern, equations[0])

        self.independent_terms = list()
        self.coefficients = list()

        for equation in equations:
            match = re.search(before_equals_pattern, equation)
            coeffs_str = match.group(0)
            coeffs_match = re.findall(coefficients_pattern, coeffs_str)
            coeffs = [float(m[1].replace(' ', '')) if m[1] else 1.0 for m in coeffs_match]
            self.coefficients.append(coeffs)

            match = re.search(indepedent_terms_pattern, equation)
            if match:
                constant_str = match.group(0)
                constant = float(constant_str.strip())
                self.independent_terms.append(constant)
        self.iterations = list()
        self.equations = None
    
    def solve(self, first_step, approximation, iterations):
        coefficients = copy.copy(self.coefficients)
        independent_terms = copy.copy(self.independent_terms)
        auxiliar = []
        iter = 0

        solution = list()
        for index in range(len(independent_terms)):
            solution.append(first_step)

        resolution = list()
        for k in range(len(solution)):
            auxiliar.append(0)

        limit = iterations

        while iter < limit:
            array_iteracao = list()
            equations_iteracao = list() # nova lista para armazenar as equações da iteração atual
            for i in range(len(coefficients)):
                x = independent_terms[i]
                equation = f"{self.variables[i]} = ({independent_terms[i]}"
                for j in range(len(coefficients)):
                    if i != j:
                        x -= coefficients[i][j]*solution[j]
                        equation += f"-{coefficients[i][j]}{self.variables[j]}"
                x /= coefficients[i][i]
                auxiliar[i] = x
                equation += f")/{coefficients[i][i]}"
                equations_iteracao.append(equation)
                array_iteracao.append(round(x, approximation))
            iter += 1
            resolution.append(array_iteracao)
            self.equations = equations_iteracao # atualiza o valor do atributo equations a cada iteração
            for p in range(len(auxiliar)):
                solution[p] = auxiliar[p]
        self.iterations = copy.copy(resolution)