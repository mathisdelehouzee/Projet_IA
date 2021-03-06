#Vendeur_1
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

class Vendeur_1(Agent):
        #ce vendeur propose la pièce boite-vitesse à un prix de 38.98, stock 50 et un avantage de 25% si le nombre de pièce demandés dépasse 3
        #(la décision de la réduction sera prise par le courtier)
        piece = "boite-vitesse"
        prix = 2 #38.98
        stock =30
        avantage=25
        CMDR = ""
        QuntD = 0

        def __init__(self, aid):
            super(Vendeur_1, self).__init__(aid=aid, debug=False)
        def on_start(self):
            super(Vendeur_1, self).on_start()
            display_message(self.aid.localname, "Demarrage de l'agent Vendeur_1 - reception des commandes en cours ...")
        #le vendeur est en écoute des courtiers
        def react(self, message):
            super(Vendeur_1, self).react(message)
            perCFP="cfp" #perCFP indique les message de type Call for proposal envoyé par le courtier
            ontoCFP="contactVend1" #ontologie des messages envoyé par le courtier 
            perAccept="accept-proposal" #indique le type d'un message lorsque le courtier a accepter une proposition
            perReject="reject-proposal" #indique l'inverse de accept-proposal ci-dessus
            super(Vendeur_1, self).react(message)
            #si le vendeur recoie une appel d'offre, il doit immediatement envoyer son offre à la veugle


            if message.performative==perCFP and message.ontology==ontoCFP:
                    if  self.stock > self.QuntD :
                        print("Vendeur_1 : Commande reçue. Tentative de vente de la piece boite-vitesse en cours ...")
                        #definir un message de type REQUEST avec un protocole FIPA_REQUEST_PROTOCOL (code en 2 instructions)
                        message = ACLMessage(ACLMessage.PROPOSE)
                        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                        message.set_sender(AID('vendeur_1'))
                        message.add_receiver(AID('courtier'))
                        #donner à votre message une ontologie "cmdacheteur"
                        message.set_ontology("piecePropose")
                        pieceV1={'piece':self.piece, 'prix' : self.prix, 'avantage' : self.avantage,'stock':self.stock}
                        obR=pickle.dumps(pieceV1)
                        message.set_content(obR)
                        self.send(message)
                    else :
                        print("Vendeur_1 : Commande reçue mais malheureusement nous n'avons plus de stock")
                        #Il faut envoyer le message pour que le courtier comprenne que le vendeur n'a rien
                        message = ACLMessage(ACLMessage.PROPOSE)
                        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                        message.set_sender(AID('vendeur_1'))
                        message.add_receiver(AID('courtier'))
                        message.set_ontology("piecePropose")
                        pieceV1={'piece':"Néant", 'prix' : self.prix, 'avantage' : self.avantage,'stock':self.stock}
                        obR=pickle.dumps(pieceV1)
                        message.set_content(obR)
                        self.send(message)

            if message.performative==perReject:
                print("Vendeur_1 : Tentative de vente refusée - peut être une autre fois\n")

            if message.performative==perAccept:
                print("Vendeur_1 : Tentative de vente acceptée - RAVIS\n \n")
                self.stock -= message.content
                print("Nouveau Stock du vendeur 1 : " , self.stock)

