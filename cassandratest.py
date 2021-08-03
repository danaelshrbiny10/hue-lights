from cassandra import cluster
from cassandra.cluster import Cluster, Session


cluster = cluster()

Session - cluster.connect('hue ligts')

Session.execute()