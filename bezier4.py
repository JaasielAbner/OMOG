class bezier4:
	def __init__(self, control_points: list, precision: int):
		self.control_points = control_points
		self.precision = precision
		self.function()		
		

	def function(self):
		self.points = []
		for t in [_/self.precision for _ in range(self.precision+1)]:
			x = pow((1-t),4) * self.control_points[0][0] + t * pow((1-t),3) * self.control_points[1][0] * 4 + pow(t,2) * pow((1-t),2) * self.control_points[2][0] * 6 + pow(t,3) * pow((1-t),1) * self.control_points[3][0] * 4 + pow(t,4) * self.control_points[4][0] 
			y = pow((1-t),4) * self.control_points[0][1] + t * pow((1-t),3) * self.control_points[1][1] * 4 + pow(t,2) * pow((1-t),2) * self.control_points[2][1] * 6 + pow(t,3) * pow((1-t),1) * self.control_points[3][1] * 4 + pow(t,4) * self.control_points[4][1] 
			self.points.append((x,y))