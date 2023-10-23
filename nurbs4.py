class NURBSCurve:
    def __init__(self, control_points: list, knots):
        self.control_points = control_points
        self.knots = knots

        if len(self.knots) != 11:
            print("Invalid knot vector length")
            exit()

    def binomial_coefficient(self, k):
        if k == 0:
            return 1
        if k < 0 or k > 4:
            return 0
        result = 1
        for i in range(1, k + 1):
            result *= (4 - i + 1) / i
        return result

    def bernstein_basis(self, i, u):
        return (
            self.binomial_coefficient(i) *
            (1 - u) ** (4 - i) *
            u ** i
        )

    def evaluate(self, u):
        curve_point = [0.0] * 2

        for i in range(5):
            basis = self.bernstein_basis(i, u)
            for j in range(2):
                curve_point[j] += self.control_points[i][j] * basis

        return curve_point

