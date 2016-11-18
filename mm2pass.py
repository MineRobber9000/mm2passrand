import logging

logging.basicConfig(filename=__name__.replace(".","/")+".py.log")
lumberjack = logging.getLogger(__name__)

class Game:
	"""A class representing a game of Mega Man 2."""
	
	robo_masters = ["Air Man","Bubble Man","Crash Man","Flash Man","Heat Man","Metal Man","Quick Man","Wood Man"]
	lookup_table = {"Air Man": [["E3","D2"],["E4","D3"],["E5","D4"],["B1","D5"],["B2","E1"]],"Bubble Man":[["D1","C3"],["D2","C4"],["D3","C5"],["D4","D1"],["D5","D2"]],"Crash Man":[["C5","E2"],["D1","E3"],["D2","E4"],["D3","E5"],["D4","B1"]],"Flash Man":[["C1","E4"],["C2","E5"],["C3","B1"],["C4","B2"],["C5","B3"]],"Heat Man": [["B2","D5"],["B3","E1"],["B4","E2"],["B5","E3"],["C1","E4"]], "Metal Man": [["E5","E1"],["B1","E2"],["B2","E3"],["B3","E4"],["B4","E5"]],"Quick Man": [["B4","C4"],["B5","C5"],["C1","D1"],["C2","D2"],["C3","D3"]],"Wood Man":[["D3","B5"],["D4","C1"],["D5","C2"],["E1","C3"],["E2","C4"]]}

	def __init__(self):
		self.etanks = 0
		self.robomasterstatus = {}
		for robo in Game.robo_masters:
			self.robomasterstatus.update({robo: False})
		lumberjack.info("Game class initiated.")

	def setETanks(self, n):
		self.etanks = n
		if self.etanks > 4:
			self.etanks = 4
		elif self.etanks < 0:
			self.etanks = 0
		lumberjack.info("E-tanks set to "+str(n)+".")

	def defeat(self, robo):
		for nrobo in self.robomasterstatus:
			if robo == nrobo:
				self.robomasterstatus.update({robo: True})
				lumberjack.info(robo+" was set to defeated.")

	def getPassword(self):
		ret = ""
		ret += "A"+str(self.etanks+1)+" "
		for robo in self.robomasterstatus:
			if self.robomasterstatus[robo]:
				ret += Game.lookup_table[robo][self.etanks][0]+" "
			else:
				ret += Game.lookup_table[robo][self.etanks][1]+" "
		return ret[:-1]

def prettify(passwordDump):
	parts = passwordDump.split(" ")
	filter(None,parts)
	a = parts[0][1:]
	parts.remove(parts[0])
	b = []
	c = []
	d = []
	e = []
	for part in parts:
		if part.find("B") == 0:
			b.append(part[1:])
		elif part.find("C") == 0:
			c.append(part[1:])
		elif part.find("D") == 0:
			d.append(part[1:])
		elif part.find("E") == 0:
			e.append(part[1:])
	b.sort()
	c.sort()
	d.sort()
	e.sort()
	print("A: "+str(a))
	print("B: "+" ".join(b))
	print("C: "+" ".join(c))
	print("D: "+" ".join(d))
	print("E: "+" ".join(e))
	lumberjack.info("Completed prettification of password dump "+passwordDump+".")
