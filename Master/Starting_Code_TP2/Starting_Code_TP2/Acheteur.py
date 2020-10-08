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
                    display_message(self.aid.localname, "Demarrage de l'agent Acheteur")
                    #donner l'instruction permettant d'appeler la fonction sending_cmd après 8.0 secondes
                    call_later(8.0,self.sending_cmd)
                    call_later(50.0,self.sending_cmd)
        def sending_cmd(self):
                    CMD = "plaquettes"
                    display_message(self.aid.localname, "Acheteur : Envoie d'une commande au courtier")
                    '''#definir un message de type REQUEST avec un protocole FIPA_REQUEST_PROTOCOL (code en 2 instructions)
                    '''
                    message = ACLMessage(ACLMessage.REQUEST)
                    message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                    #donner l'agent expediteur (acheteur) et l'agent recepteur (courtier) (code en 2 instructions)
                    message.set_sender(AID('acheteur')) #fournisseur: nom de l’agent expéditeur
                    message.add_receiver(AID('courtier')) 
                    #donner à votre message une ontologie "cmdacheteur"
                    message.set_ontology("cmdacheteur")
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
                    display_message(self.aid.localname, "Acheteur : Envoie d'une commande au  : Fait")
                    self.send(message)

        def react(self, message):
                    onto="decision" #onto presente les messages de courtier avec une decision final 
                    perOK="agree" #perOk indique un message avec une performative agree (achat ok)
                    perNotOK="reject-proposal" #perNotOk indique un message avec performative reject-proposal (achat not ok)
                    super(Acheteur, self).react(message)
                    '''via deux instruction if, gérer les conditions d'un achat terminé avec succès ou l'inverse '''
                    if message.ontology==onto and message.performative==perOK :
                        print('Yes, je peux acheter')
                    if message.ontology==onto and message.performative==perNotOK:
                        print("Bande d'incapables, vousn'avez pas réussi à trouver ce que je voulais")
                   
