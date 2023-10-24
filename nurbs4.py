class NURBSCurve:
    def __init__(self, control_points: list, knots: list, precision: int):
        self.precision = precision
        self.control_points = control_points
        self.knots = knots
        self.function()

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

    def function(self):
        self.points = []

        for t in [_/self.precision for _ in range(self.precision+1)]:
            curve_point = [0.0] * 2
            for i in range(5):
                basis = self.bernstein_basis(i, t)
                for j in range(2):
                    curve_point[j] += self.control_points[i][j] * basis
            self.points.append(curve_point)

    def updateControlPoints(self, control_points: list):
        self.control_points = control_points
        self.function()
