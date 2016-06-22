from sys import argv

import spade

from agent import Agent

class CoordinatorAgent(Agent):
	def _setup(self):
		print "MyAgent starting . . ."

		self.answers = {}

		template = spade.Behaviour.ACLTemplate()
		template.setSender(spade.AID.aid(self.name,["xmpp://{}".format(self.name)]))
		selfTemplate = spade.Behaviour.MessageTemplate(template)

		template = spade.Behaviour.ACLTemplate()
		template.setOntology('poker')
		pokerTemplate = spade.Behaviour.MessageTemplate(template)

		self.addBehaviour(self.AnswerBehav(), pokerTemplate)
		self.addBehaviour(self.RequestBehav(), selfTemplate)
		self.addBehaviour(self.FindAgentsBehav(), None)


if __name__ == "__main__":
	a = CoordinatorAgent("coordinator@127.0.0.1", "secret")

	args = ' '.join(argv[1:])
	a.content = args or "spade:2 diamond:j heart:k heart:q"
	a.finished = False
	a.start()
	try:
		while not a.finished:
			pass
	except KeyboardInterrupt:
		pass

	a.stop()
	print 'Answers:\n{}'.format(a.answers)
