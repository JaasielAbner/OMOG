class bezier4:
	def __init__(self,control_points: list, precision: int):
		self.control_points = control_points
		self.precision = precision
		self.points = []
		ts = [t/precision for t in range(precision+1)]
		for t in ts:
			x =  ((1-t)**3) * control_points[0][0] + 3*t*((1-t)**2) * control_points[1][0] + 3*(1-t)*(t**2) * control_points[2][0] + (t ** 3) * control_points[3][0]
			y =  ((1-t)**3) * control_points[0][1] + 3*t*((1-t)**2) * control_points[1][1] + 3*(1-t)*(t**2) * control_points[2][1] + (t ** 3) * control_points[3][1]
			self.points.append((x,y))

	def get_points(self):
		return self.points