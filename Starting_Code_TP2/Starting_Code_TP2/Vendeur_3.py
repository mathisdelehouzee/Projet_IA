#Vendeur_3
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

class Vendeur_3(Agent):
        #ce vendeur propose la pièce plaquettes à un prix de 33.98, stock 80 et un avantage de 30% si le nombre de pièce demandés dépasse 3 
        #(la décision de la réduction sera prise par le courtier)
        #malgré que le prix de plaquette est plus elevé cher le vendeur_3 par rapport au Vendeur_2, l'avantage est plus interessant si le nombre de pèce dépasse 3.
        piece = "plaquettes"
        prix = 33.98
        stock =80
        avantage = 25
        def __init__(self, aid):
            super(Vendeur_3, self).__init__(aid=aid, debug=False)
        def on_start(self):
            super(Vendeur_3, self).on_start()
            display_message(self.aid.localname, "Demarrage de l'agent Vendeur_3 - reception des commandes en cours ...")

        def react(self, message):
          '''insperez vous de la classe Vendeur_1 pour donner les instructions du Vendeur_2 suite à la reception des messages de courtier'''
            message = ACLMessage(ACLMessage.PROPOSE)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.set_sender(AID('vendeur_3'))
            message.add_receiver(AID('courtier'))
            #donner à votre message une ontologie "cmdacheteur"
            message.set_ontology('piecePropose')
            pieceV1={'prix' : prix, 'avantage' : avantage}
            obD=pickle.dumps(pieceV1)
            message.set_content(obD)
            self.send(message)