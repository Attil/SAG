from agent import Agent
import spade

class SolverAgent(Agent):
	def _setup(self):
		print "MyAgent starting . . ."
		self.addBehaviour(self.RegisterServiceBehav(), None)

		template = spade.Behaviour.ACLTemplate()
		template.setOntology('poker')
		t = spade.Behaviour.MessageTemplate(template)

		self.addBehaviour(self.PerformBehav(), t)

	def interpret(self, content):
		return self.solve(content.split())

	def solve(self, elements):
		raise NotImplementedError

if __name__ == "__main__":
	a = SolverAgent("solver@127.0.0.1", "secret")
	a.start()
	try:
		while True:
			pass
	except KeyboardInterrupt:
		a.stop()
