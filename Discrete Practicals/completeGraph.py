def is_complete_graph(adj_matrix):
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and adj_matrix[i][j] != 1:
                return False
    return True        
num_vertices=int(input("Enter no. of vertex :"))
# graph =[
#          [0 ,1,0,1],
#          [1,0,1,1],
#          [1,1,0,1],
#          [1,1,1,0]
#                     ]

graph=[]
for k in range (num_vertices):
    row =[]
    for l in range (num_vertices):
        value = int(input(f"enter the value of vertex {k}{l} :"))
        row.append(value)
    graph.append(row)    
        
print(graph)
is_complete_graph(graph)
if is_complete_graph(graph):
    print("it's a complete graph")
else:
    print("It's not a complete graph")    

