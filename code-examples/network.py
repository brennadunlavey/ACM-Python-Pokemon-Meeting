# Using the given data set, display relationships between people based on degrees and salaries

import networkx as nx 
import matplotlib.pyplot as plt

myObj = [
    {'name': 'Alice', 'degree': 'cs', 'gpa': 3.5, 'age': 25, 'salary': 55000},
    {'name': 'Bob', 'degree': 'ee', 'gpa': 3.9, 'age': 43, 'salary': 120000},
    {'name': 'Craig', 'degree': 'me', 'gpa': 3.2, 'age': 19, 'salary': 30000},
    {'name': 'Daphne', 'degree': 'ee', 'gpa': 3.8, 'age': 39, 'salary': 70000},
    {'name': 'Edward', 'degree': 'me', 'gpa': 4.0, 'age': 51, 'salary': 95300},
    {'name': 'Fred', 'degree': 'cs', 'gpa': 2.8, 'age': 23, 'salary': 35750},
    {'name': 'Gertrude', 'degree': 'cs', 'gpa': 3.4, 'age': 31, 'salary': 105350},
    {'name': 'Harry', 'degree': 'ee', 'gpa': 3.2, 'age': 46, 'salary': 150500},
    {'name': 'Isabel', 'degree': 'cs', 'gpa': 3.0, 'age': 39, 'salary': 51400},
    {'name': 'Justin', 'degree': 'me', 'gpa': 2.5, 'age': 55, 'salary': 120100},
    {'name': 'Kaden', 'degree': 'cs', 'gpa': 1.9, 'age': 21, 'salary': 95000}
]

    
# Create an edge between every pair of people who either have the same degree or a similar salary
g = nx.Graph()
for i,p1 in enumerate(myObj):
    for j,p2 in enumerate(myObj):
        if i > j and (p1['degree'] == p2['degree'] or abs(p1['salary'] - p2['salary']) <= 10000):
            g.add_edge(i,j)

# Briefly perform a builtin algorithm to organize the graph
pos = nx.spring_layout(g,iterations=10, weight="strength", seed=2)


# Draw the graph using matplotlib
plt.figure()
nodes = list(g.nodes)
# nodeColors = ['tab:red','tab:orange','tab:green','tab:blue']

# Determine the size of each node by salary, and its color by gpa
nodeSizes = [5+200*obj['salary']/200000 for obj in myObj]
nodeColors = ['tab:red' if obj['gpa'] < 3.2 else 'tab:blue' for obj in myObj]

nx.draw_networkx_nodes(g,nodelist=nodes, pos=pos, node_size=nodeSizes, node_color=nodeColors)

nx.draw_networkx_edges(g,pos=pos)

# display plot
plt.title('Cool Graph!')
plt.show()
plt.savefig('code-examples/outputs/network-graph')
print('Network graph saved in code-examples/outputs!')



