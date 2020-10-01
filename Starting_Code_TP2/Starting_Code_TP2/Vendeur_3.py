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
             perCFP="cfp" #perCFP indique les message de type Call for proposal envoyé par le courtier
             ontoCFP="contactVend3" #ontologie des messages envoyé par le courtier
             perAccept="accept-proposal" #indique le type d'un message lorsque le courtier a accepter une proposition
             perReject="reject-proposal" #indique l'inverse de accept-proposal ci-dessus
             super(Vendeur_3, self).react(message)
             if message.performative==perCFP and message.ontology==ontoCFP:
                    print("Vendeur_3 : Commande recu Tentative de vente de la piece plaquettes en cours ...")
                    message = ACLMessage(ACLMessage.PROPOSE)
                    message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                    message.set_sender(AID('vendeur_3'))
                    message.add_receiver(AID('courtier'))
                    #donner à votre message une ontologie "cmdacheteur"
                    message.set_ontology('piecePropose')
                    pieceV3={'piece':self.piece, 'prix' : self.prix, 'avantage' : self.avantage}
                    obR=pickle.dumps(pieceV3)
                    message.set_content(obR)
                    self.send(message)

             if message.performative==perReject:
                    print("Vendeur_3 : Tentative de vente refusée - peut être une autre fois\n")

             if message.performative==perAccept:
                    print("Vendeur_3 : Tentative de vente acceptée - RAVIS\n \n")