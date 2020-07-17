class cCollider:
	def __init__(self):
		self.rectList = []
		self.rects = {}
	def renderColliders(self):
		for name in range(0,len(self.rectList)):
			self.rectList[name].create(self.rects)
	def createColliders(self):
		import rectClass
		for name in self.rects:
			self.rectList.append(rectClass.colission(self.rects[name][0][0],self.rects[name][0][1],
									self.rects[name][0][2],self.rects[name][0][3],
									self.rects[name][2],
									self.rects[name][1],
									self.rects))
	def loadPickle(self):
		import pickle
		print("OPENING PICKLE MAP FILE")
		pickleIN = open("maps/map1.pickle", "rb")
		self.rects = pickle.load(pickleIN)
		pickleIN.close()