import spade

class Agent(spade.Agent.Agent):
    class FindAgentsBehav(spade.Behaviour.OneShotBehaviour):
        def onStart(self):
            print "Finding Agents..."

        def _process(self):
            dad = spade.DF.DfAgentDescription()
            results = self.myAgent.searchService(dad)
            self.myAgent.receivers = []
            for result in results:
                self.myAgent.receivers.append(result.name.getName())

            print 'Found services: {}'.format(self.myAgent.receivers)
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid(self.myAgent.name, ['xmpp://{}'.format(self.myAgent.name)]))
            msg.setContent("foundServices")

            self.myAgent.send(msg)

        def onEnd(self):
            print "Finished finding agents..."


    class RegisterServiceBehav(spade.Behaviour.OneShotBehaviour):
		def onStart(self):
			print "Registering service..."

		def _process(self):
			sd = spade.DF.ServiceDescription()
			sd.setName("abc")
			sd.setType("solver")
			dad = spade.DF.DfAgentDescription()
			dad.addService(sd)
			dad.setAID(self.myAgent.getAID())
			res = self.myAgent.registerService(dad)
			print "Service Registered"

		def onEnd(self):
			print "Finished registering service..."


    class RequestBehav(spade.Behaviour.EventBehaviour):
        def onStart(self):
            print "Broadcasting the request..."

        def _process(self):
            self.msg = spade.ACLMessage.ACLMessage()
            self.msg.setPerformative('request')
            self.msg.setOntology('poker')
            self.msg.setLanguage('OWL-S')
            self.msg.setContent(self.myAgent.content)

            print 'I will request: {}'.format(self.myAgent.receivers)

            for receiver in self.myAgent.receivers:
                print 'Requesting {}...'.format(receiver)
                aid = spade.AID.aid(name=receiver, addresses=['xmpp://{}'.format(receiver)])
                self.msg.addReceiver(aid)

            self.myAgent.send(self.msg)

        def onEnd(self):
            print "Finished broadcasting the request!"


    class PerformBehav(spade.Behaviour.Behaviour):
        def onStart(self):
            print "Getting a request..."

        def _process(self):
            print 'Waiting for a message...'

            self.msg = self._receive(True)

            if self.msg:
                print "Got message!"
            else:
                print "Didn't get message"

            result = self.myAgent.interpret(self.msg.content)

            response = self.msg.createReply()
            response.setContent(result)

            self.myAgent.send(response)

        def onEnd(self):
            print "Fulfilled a request!"

    class AnswerBehav(spade.Behaviour.Behaviour):
        def onStart(self):
            print "Getting an answer..."

        def _process(self):
            print 'Waiting for an answer...'

            self.msg = self._receive(True)

            if self.msg:
                print "Got answer! {} said: {}".format(self.msg.getSender().getName(), self.msg.getContent())
                self.myAgent.answers[self.msg.getSender().getName()] = self.msg.getContent()

                if len(self.myAgent.receivers) == len(self.myAgent.answers):
                    print 'Got all answers!'
                    self.myAgent.finished = True

        def onEnd(self):
            print "Finished listening for answers!"
