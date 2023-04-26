import pandas as pd 
import networkx as nx 
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/yrink/Desktop/Experiments/pseudo_facebook.csv") 
print(df. head( ))

# Load edge list 
fb_graph=nx.from_pandas_edgelist(df,source="age", target="dob_year") type(fb_graph)
                                 
print('Display all the Edges') 
print(fb_graph.edges())
                                 
print('Display all the nodes') 
print(fb_graph.nodes())
                                 
print('Add new node in graph') 
                                 
fb_graph.add_edge("123","2154") 
                                 
print(fb_graph.nodes()) 

G=nx.Graph(fb_graph)
                                 
print('Visualization of network')
                                 
nx.draw(fb_graph,with_labels=True)
plt.show()

print('Degree of each node') 
print(nx.degree(fb_graph))

print('degree of a particular node') 
print(nx.degree(fb_graph,1999))

print('degree centrality') 
print(nx.degree_centrality(fb_graph))

print('sort degree centrality') 
print(sorted(nx.degree_centrality(fb_graph).values()))

print('Display influential node') 
m_influential=nx.degree_centrality(G) for w in
sorted(m_influential,key=m_influential.get,reverse=True): print(w,m_influential[w])
print('Find Betweenness centrality')

pos=nx.spring_layout(G) 
betCent=nx.betweenness_centrality(G,normalized=True,endpoints=True) 
node_color=[20000.0*G.degree(v)for v in G] 
node_size=[v*10000 for v in betCent.values()] 
print(plt.figure(figsize=(20,20))) 
print(nx.draw_networkx(G,pos=pos,with_labels=False,node_color=node_color,node_size=node_size)) 
print(sorted(betCent,key=betCent.get,reverse=True)[:5]) plt.show()

print('closeness centrality') 
closeness_centrality=nx.centrality.closeness_centrality(G)
print((sorted(closeness_centrality.items(),key=lambda item:item[1],reverse=True))[:8])

print('Find Density of a network') 
node_size=[v*50 for v in closeness_centrality.values()] 
plt.figure(figsize=(15,8)) 

print('degree centrality') 
print(nx.degree_centrality(fb_graph))
print('sort degree centrality') 

print(sorted(nx.degree_centrality(fb_graph).values()))
print('Display influential node') 

m_influential=nx.degree_centrality(G) 
for w in
sorted(m_influential,key=m_influential.get,reverse=True): print(w,m_influential[w])
  
print('Find Betweenness centrality') 
pos=nx.spring_layout(G) 
betCent=nx.betweenness_centrality(G,normalized=True,endpoints=True) 

node_color=[20000.0*G.degree(v)for v in G] 
node_size=[v*10000 for v in betCent.values()] 

print(plt.figure(figsize=(20,20))) 
print(nx.draw_networkx(G,pos=pos,with_labels=False,node_color=node_color,node_size=node_size)) 

print(sorted(betCent,key=betCent.get,reverse=True)[:5]) plt.show()

print('closeness centrality') 
closeness_centrality=nx.centrality.closeness_cent rality(G)

print((sorted(closeness_centrality.items(),key=la mbda item:item[1],reverse=True))[:8])
print('Find Density of a network') 

node_size=[v*50 for v in closeness_centrality.values()] 
plt.figure(figsize=(15,8)) 

print('Remove node') 
G = nx.path_graph(8) 
print(list(G.edges))

print('After removing Node') 
G = nx.path_graph(8) 
print(list(G.edges))

print('Remove edges')
G = nx.path_graph(8) # or DiGraph, etc 
G.remove_edge(0, 1) 
print(list(G.edges))

print('Clustering') 
print(nx.clustering(G))

print('Community detection') 
#Edge betweenness lst_b =nx.algorithms.community.girvan_newman(fb_graph) type(lst_b) #Print possible communities for 
x in lst_b: print(x)
  
  


