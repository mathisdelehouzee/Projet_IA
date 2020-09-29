#Acheteur
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

class Acheteur(Agent):
    def __init__(self, aid):
        super(Acheteur, self).__init__(aid=aid, debug=False)
    def on_start(self):
        super(Acheteur, self).on_start()
        display_message(self.aid.localname, "Demarrage de l'agent Vendeur_1 - reception des notes en cours ...")
        #donner l'instruction permettant d'appeler la fonction sending_cmd après 8.0 secondes
        '''
        -->
        '''

    def sending_cmd(self):
        CMD = "plaquettes"
        display_message(self.aid.localname, "Acheteur : Envoie d'une commande au courtier")
        '''#definir un message de type REQUEST avec un protocole FIPA_REQUEST_PROTOCOL (code en 2 instructions)
        -->
        -->
        '''
        
        '''#donner l'agent expediteur (acheteur) et l'agent recepteur (courtier) (code en 2 instructions)
        -->
        -->
        '''
        '''#donner à votre message une ontologie "cmdacheteur"
        -->
        '''
        '''
        Le contenu à envoyer est présenté par un objet {piece, quantité}  
        la fonction pickle de python permet d'englober cette objet et de l'envoyer facilement avec message.set_content
        '''
        pieceD={'piece' : "plaquettes", 'quantitie' : 3}
        obD=pickle.dumps(pieceD)
        message.set_content(obD)
        '''
        --> acter l'envoie du message
        '''
        self.send(message)

    def react(self, message):
        onto="decision" #onto presente les messages de courtier avec une decision final 
        perOK="agree" #perOk indique un message avec une performative agree (achat ok)
        perNotOK="reject-proposal" #perNotOk indique un message avec performative reject-proposal (achat not ok)
        super(Acheteur, self).react(message)
        '''via deux instruction if, gérer les conditions d'un achat terminé avec succès ou l'inverse '''
       
