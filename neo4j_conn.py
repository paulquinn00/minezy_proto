import sys
import traceback
from py2neo import Graph

g_session = None

def connect(createConstraints=False):
	global g_session
	
	try:
		sys.stdout.write("Connect to Neo4j... ")
		g_session = Graph()
		sys.stdout.write("OK\n")
		
		if createConstraints:
			create_constraints()
			
		return g_session
	except:
		print
		print "Error:", sys.exc_info()[1]
		exit(1)
		
	return None


def create_constraints():
	try:
		tx = g_session.cypher.begin()
		
		sys.stdout.write("accounts index... ")
		tx.append("CREATE CONSTRAINT ON (a:Account) ASSERT a.id IS UNIQUE")
		tx.process()
		
		sys.stdout.write("contacts index... ")
		tx.append("CREATE CONSTRAINT ON (c:Contact) ASSERT c.email IS UNIQUE")
		tx.process()
		
		sys.stdout.write("email index... ")
		tx.append("CREATE CONSTRAINT ON (e:Email) ASSERT e.id IS UNIQUE")
		tx.process()
		
		sys.stdout.write("names index... ")
		tx.append("CREATE CONSTRAINT ON (n:Name) ASSERT n.name IS UNIQUE")
		tx.process()
		
		sys.stdout.write("years index... ")
		tx.append("CREATE CONSTRAINT ON (y:Year) ASSERT y.num IS UNIQUE")
		tx.process()
		
		sys.stdout.write("months index... ")
		tx.append("CREATE CONSTRAINT ON (m:Month) ASSERT m.num IS UNIQUE")
		tx.process()
		
		sys.stdout.write("days index... ")
		tx.append("CREATE CONSTRAINT ON (d:Day) ASSERT d.num IS UNIQUE")
		tx.process()
		
		sys.stdout.write("word index... ")
		tx.append("CREATE CONSTRAINT ON (w:Word) ASSERT w.id IS UNIQUE")
		tx.commit()

		sys.stdout.write("OK\n")
	except:
		print
		print "Error:", sys.exc_info()[1]
		traceback.print_exc()

	