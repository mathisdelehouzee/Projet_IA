#Courtier
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

class Courtier(Agent):
	CMDR = "" #variable qui va prendre la valeur de la csommande de l'acheteur
	QuntD =0 #variable qui va prendre la valeur de la quantité demandé par l'acheteur
	decFinal=0 #variable qui va verifier si la commande de l'acheteur correspond à l'un des meilleures offres de marchée
	nbrpro =0 #variable qui va compter le nombre d'article similaire (avec prix different)
	PrixFinal=0 # le toral du prix selon la quantité demandé, une réduction de 30% est appliqué sur le total, si quantité est > =3
	IdBestVendeur="" #cette variable va contenir le l'ID du meilleure vendeur en se basant sur la meilleure offre
	LesVendeurs= [] # cette liste va stocker les Id des vendeurs qui envoient une offre correspondante à la demande de l'acheteur. 
	listPrix = [] #cette liste va sotocker les prix totaux de chaque offe correspondante à la demande de l'achetuer pour selectionner le prix total minimal
	def __init__(self, aid):
		super(Courtier, self).__init__(aid=aid, debug=False)
	def on_start(self):
		super(Courtier, self).on_start()
		display_message(self.aid.localname, "Demarrage de l'agent Courtier")
    #donner la définition de la fonction contact_vend1 permettant de contacter le vendeur Num1 
	def contact_vend1(self):
		print ("contact vendeur N° 1 en cours ... ")
		'''#definir un message de type CFP avec un protocole FIPA_REQUEST_PROTOCOL (code en 2 instructions) '''
		message = ACLMessage(ACLMessage.CFP)
		message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
		'''#donner l'agent expediteur (courtier) et l'agent recepteur (vendeur_1) (code en 2 instructions)'''
		message.set_sender(AID('courtier')) 
		message.add_receiver(AID('vendeur_1'))
		'''#donner à votre message une ontologie "contactVend1" et un contenu Courtier.CMDR (initialsé à la réception d'une commande) et envoyer le message (code en 3 instructions)'''
		message.set_ontology('contactVend1')
		message.set_content(Courtier.CMDR)
		self.send(message)
	def contact_vend2(self):
		print ("contact vendeur N° 2 en cours ... ")
		'''#definir un message de type CFP avec un protocole FIPA_REQUEST_PROTOCOL (code en 2 instructions)'''
		message=ACLMessage(ACLMessage.CFP)
		message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
		'''#donner l'agent expediteur (courtier) et l'agent recepteur (vendeur_2) (code en 2 instructions)'''
		message.set_sender('courtier')
		message.add_receiver('vendeur_2')
		'''#donner à votre message une ontologie "contactVend2" et un contenu Courtier.CMDR (initialsé à la réception d'une commande) et envoyer le message (code en 3 instructions) '''
		message.set_ontology('contactVend2')
		message.set_content(Courtier.CMDR)
		self.send(message)
	def contact_vend3(self):
		print ("contact vendeur N° 3 en cours ... ")
		'''#definir un message de type CFP avec un protocole FIPA_REQUEST_PROTOCOL (code en 2 instructions) '''
		message=ACLMessage(ACLMessage.CFP)
		message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            
		'''#donner l'agent expediteur (courtier) et l'agent recepteur (vendeur_3) (code en 2 instructions)'''
		message.set_sender('courtier')
		message.add_receiver('vendeur_3')
		'''#donner à votre message une ontologie "contactVend3" et un contenu Courtier.CMDR (initialsé à la réception d'une commande) et envoyer le message (code en 3 instructions) '''
		message.set_ontology('contactVend3')
		message.set_content(Courtier.CMDR)
		self.send(message)

	def contact_Acheteur(self):
		print ("contact de Acheteur en cours ... ")
		if Courtier.decFinal==0:
			message=ACLMessage(ACLMessage.REJECT_PROPOSAL)
			message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
			message.set_content("pas d'offres trouvées")

		if Courtier.decFinal==1:
			message=ACLMessage(ACLMessage.AGREE)
			message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
			message.set_content("Meilleure offre trouvée")
		message.set_sender('courtier')
		message.add_receiver('acheteur')
		message.set_ontology('decision')
		self.send(message)

    #l'agent couriter est en écoute permanent grâce à la fonction react ci-dessous :
	def react(self, message):
         percmd="request" #type des messages envoyés par l'acheteur
         ontocmd="cmdacheteur" #ontologie des messages envoyés par l'acheteur
         perVend="propose" #type des messages envoyés par les vendeurs
         ontoVend="piecePropose" #ontologie des messages envoyés par les vendeurs
         super(Courtier, self).react(message)
    #Si un message est reçu d'un acheteur : 
         if message.performative==percmd and message.ontology==ontocmd:
            display_message(self.aid.localname, 'Courtier !! : Message recu de : {}'.format(message.sender.name))
            '''
                puisque la commande du client est un objet, il faut passer par pickle pour déchiffrer le message. 
                initialiser les deux variables globales CMDR (commande recu) et QuntD (quantité demandé) 
                comme suite :
            '''
            pieceD = message.content
            obD = pickle.loads(pieceD)
            Courtier.CMDR = obD['piece']
            Courtier.QuntD = obD['quantitie']
            '''
                Affichage des information de la commande recu :  
            '''

            print("\nLa commande recu de l'acheteur est : ", Courtier.CMDR)
            print("La quantitie demande est : ",Courtier.QuntD)
            print("Contact des vendeurs en cours ...\n")
            '''
                en 3 instructions, utilisez call_latter pour contacter les vendeur1, vendeur2 et vendeur3 (appel des fonctions ci-dessus)
                -->premier appel après 5.0 secondes
                -->2ème appel après 8.0 secondes
                -->3ème appel après 11.0 secondes
            '''
            call_later(5.0,self.contact_vend1)
            call_later(8.0,self.contact_vend2)
            call_later(11.0,self.contact_vend3)
    #Si un message est reçu d'un vendeur : 
         if message.performative==perVend and message.ontology== ontoVend:
            display_message(self.aid.localname, 'Courtier !! : Message recu de : {}'.format(message.sender.name))
            tempV=message.sender.name
            '''
                puisque l'offre des vendeurs est aussi un objet, il faut passer par pickle pour déchiffrer le message. 
                initialiser les deux variables globales pieceR (Piece recu) et prix, et avantage 
                -->insperez vous de l'exemple ci-dessus pour déchiffrer le message
                -->Afficher la pièce de l'offre, son prix et l'avantage réçus en 3 instructions
                '''
            pieceR = message.content
            obR = pickle.loads(pieceR)
                #Si pièce demandé correspond à la pièce de l'offre :
            if Courtier.CMDR==obR['piece']:
                    #il faut compter combier de fois l'offre est similaire à la demande (à chaque réception du message)
                Courtier.nbrpro +=1

                    #une reduction selon l'avantage envoyé de  chaque vendeur s'applique sur le prix total si la quantité demandé dépasse 3.
                if Courtier.QuntD >=3:
                        Courtier.PrixFinal= ((obR['prix']*(100-obR['avantage'])/100)*Courtier.QuntD)
                        Courtier.listPrix.append(Courtier.PrixFinal) #sotocker les prix
                        Courtier.LesVendeurs.append(message.sender.localname) #stocker les vendeurs pour que les indices des listes prix et vendeurs soient correspondantes
                        Courtier.IdBestVendeur = message.sender.localname #par défaut on suppose que ce vendeur est le meilleur
                        print("Courtier : Reduction grace à l'avantage du vendeur est appliquée, nouveau prix est : ",Courtier.PrixFinal, " au lieu de : ", Courtier.QuntD*obR['prix'])
                        print("\n****** Cette propostion correspond à la demande *****")
                        print ("\nNombre de propositions similaires est ", Courtier.nbrpro)

                        #si il exisite plusieurs offres qui correspond à la demande il faut selectionner le meilleur prix et le meilleur vendeur
                        if Courtier.nbrpro>1:
                            if Courtier.listPrix[0]>Courtier.listPrix[1]:
                                Courtier.IdBestVendeur = Courtier.LesVendeurs[1]
                                i=0
                                Courtier.PrixFinal=Courtier.listPrix[1]
                            else:
                                Courtier.IdBestVendeur = Courtier.LesVendeurs[0]
                                i=1
                                Courtier.PrixFinal=Courtier.listPrix[0]
                        
                            print ("***** la meilleur offre est de ", Courtier.PrixFinal, " proposé par le vendeur : ",Courtier.IdBestVendeur)
    	         
                            '''contacter le bestVendeur en lui envoyant ACCEPT
                        -->
                        ...
                        -->
                            '''
                            message=ACLMessage(ACLMessage.ACCEPT_PROPOSAL)
                            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                            message.set_sender('courtier')
                            message.add_receiver(AID(Courtier.IdBestVendeur))
                            message.set_ontology('repProp')
                            message.set_content('accept')
                            self.send(message)
                            message=ACLMessage(ACLMessage.REJECT_PROPOSAL)
                            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                            message.set_sender('courtier')
                            message.add_receiver(Courtier.LesVendeurs[i])
                            message.set_ontology('repProp')
                            message.set_content('Reject')
                            self.send(message)
                            Courtier.decFinal =1
                        #contacter l'acheteur ici via call_latter après 20 secondes !!!
                            '''
                        -->
                            '''
                            call_later(20.0,self.contact_Acheteur)
                            print("\n")
                    #si la quantité demandé ne depasse pas 3 :
                else:
                     Courtier.PrixFinal = obR['prix']*Courtier.QuntD
                     print("Aucune reduction n'est appliquée, prix final est : ",Courtier.PrixFinal)
                     print("\n****** Cette propostion correspond à la demande *****")
                     print ("\nNombre de propositions similaires est ", Courtier.nbrpro)
                     print("\nEnvoie de ACCEPT_PROPOSAL")
                     if Courtier.nbrpro>1:
                        if Courtier.listPrix[0]>Courtier.listPrix[1]:
                            Courtier.IdBestVendeur = Courtier.LesVendeurs[1]
                            i=0
                            Courtier.PrixFinal=Courtier.listPrix[1]
                        else:
                            Courtier.IdBestVendeur = Courtier.LesVendeurs[0]
                            Courtier.PrixFinal=Courtier.listPrix[0]
                            i=1
                        print ("***** la meilleur offre est de ", Courtier.PrixFinal, " proposé par le vendeur : ",Courtier.IdBestVendeur)
    	        #même au cas où y a pas de réduction de prix, de même qu'au dessus, il faut chercher le bestPrix et le BestVendeur en répetant exactement les même instructions que dans le if précidant
                     '''contacter le bestVendeur en lui envoyant ACCEPT
                        -->
                        ...
                        -->
                     '''
                     message=ACLMessage(ACLMessage.ACCEPT_PROPOSAL)
                     message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                     message.set_sender('courtier')
                     message.add_receiver(AID(Courtier.IdBestVendeur))
                     message.set_ontology('repProp')
                     message.set_content('accept')
                     self.send(message)
                     message=ACLMessage(ACLMessage.REJECT_PROPOSAL)
                     message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                     message.set_sender('courtier')
                     message.add_receiver(Courtier.LesVendeurs[i])
                     message.set_ontology('repProp')
                     message.set_content('Reject')
                     self.send(message)
                     call_later(20.0,self.contact_Acheteur)
                                                #Si l'offre ne correspond pas à la demande
            else:
                print("\n!!!!!!!!! Cette propostion ne correspond pas à la demande !!!!!!" )
                message=ACLMessage(ACLMessage.REJECT_PROPOSAL)
                message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
                message.set_sender('courtier')
                message.add_receiver(tempV)
                message.set_ontology('repProp')
                message.set_content('Reject')
                self.send(message)
