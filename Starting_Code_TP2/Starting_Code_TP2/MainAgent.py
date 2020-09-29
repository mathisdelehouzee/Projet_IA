#MainAgents

from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

from Courtier import Courtier
from Vendeur_1 import Vendeur_1
from Vendeur_2 import Vendeur_2
from Vendeur_3 import Vendeur_3
from Acheteur import Acheteur


if __name__ == '__main__':
    agents = list()
    port = int(argv[1])
    #cela est le code pour démarrer le vendeur num 1 :
    vendeur_1 = Vendeur_1(AID(name='vendeur_1@localhost:{}'.format(port)))
    agents.append(vendeur_1)
    print("Attention !!! : créé d'abord vos agents ")
    #donnez de la même façon le code pour le démarrage de vendeur num 2 avec le nom local vendeur_2

    #donnez de la même façon le code pour le démarrage du vendeur num 3 avec le nom local vendeur_3

    #donnez de la même façon le code pour le démarrage de l'agent courtier avec le nom local courtier

    #donnez de la même façon le code pour le démarrage de l'agent acheteur avec le nom local acheteur

    start_loop(agents)
