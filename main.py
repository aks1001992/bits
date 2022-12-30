class Graph:

	"""
	This question Community Detection is a special case of Connected Comopnent of Graph
	The overall time complexity of the Algorithm is O(V + E) where V is number of vertices and E is edges
	Auxiliary Space used by Lagorithm is O(V)

	"""
	def __init__(self, edges):
		# Edges contains all vertices of the Graph
		self.edges = edges
		self.adj = dict()
		for i in self.edges:
			self.adj[i]=[]
			
	# Simple DFS Algorithm 
	def dfsUtil(self, temp, v, visited):
		visited[v] = True
		temp.append(v)
		for i in self.adj[v]:
			if visited[i]==False:
				temp = self.dfsUtil(temp, i, visited)
		return temp

	def addEdge(self, u, v):
		self.adj[v].append(u)
		self.adj[u].append(v)

	def connectedComponent(self):
		visited = dict()
		cc = []
		for i in self.edges:
			visited[i] = False

		for i in self.edges:
			if visited[i] == False:
				temp = []
				res = self.dfsUtil(temp, i, visited)
				#res.sort() # Uncomment it if answer is required in order
				cc.append(res)
		return cc

def main():
	l = []
	with open('inputPS06.txt') as f:
		lines = f.readlines()
		for val in lines:
			val = val.replace("\n", "")
			l.append(val.split("/"))
	s = set()
	for val in l:
		a,b = val
		s.add(a)
		s.add(b)
	g = Graph(s)
	for val in l:
		a,b = val
		g.addEdge(a, b)
	cc = g.connectedComponent()
	#cc.sort() # Uncomment it if answer is required in order
	counter = 1
	with open("outputPS06.txt", "w") as f:
		for val in cc:
			n = len(val)
			temp_str = ",".join(val)
			res_str = f"Group {counter}: There are {n} participants in the group and they are {temp_str}"
			f.write(res_str)
			f.write("\n")
			counter += 1

if __name__ == "__main__":
	main()