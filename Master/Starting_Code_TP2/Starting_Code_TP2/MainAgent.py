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
        port += 1
        print("Agent vendeur 1 créé ")
        vendeur_2 = Vendeur_2(AID(name='vendeur_2@localhost:{}'.format(port)))
        agents.append(vendeur_2)
        port += 1
        print("Agent vendeur 2 créé ")
        vendeur_3 = Vendeur_3(AID(name='vendeur_3@localhost:{}'.format(port)))
        agents.append(vendeur_3)
        port += 1
        print("Agent vendeur 3 créé ")
        courtier = Courtier(AID(name='courtier@localhost:{}'.format(port)))
        agents.append(courtier)
        port += 1
        print("Agent courtier créé ")
        acheteur = Acheteur(AID(name='acheteur@localhost:{}'.format(port)))
        agents.append(acheteur)
        print("Agent acheteur créé ")

        start_loop(agents)
