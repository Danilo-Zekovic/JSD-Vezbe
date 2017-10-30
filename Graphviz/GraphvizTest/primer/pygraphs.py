'''
Created on Dec 21, 2014
@author: xxx
'''

from pydot import Node, Edge, Dot, Subgraph

# graph = Dot(graph_type = "graph") #graph_type  - graph ili digraph
# node1 = Node("a")
# node2 = Node("b")
# node3 = Node("c");
# edge1 = Edge(node1, node2)
# edge2 = Edge(node2, node3)
# edge3 = Edge(node1, node3)
# graph.add_edge(edge1)
# graph.add_edge(edge2)
# graph.add_edge(edge3)
# graph.write_png("primer1_graph.png")
 
 
graph = Dot(graph_type = "digraph", rankdir = "BT")
graph.set_node_defaults(style = "filled", fillcolor = "grey")
node1 = Node("Nastavnik", color = "green")
node2 = Node("Student", color = "blue")
node1.set("shape", "record")
graph.add_node(node1)
graph.add_node(node2)
edge1 = Edge(node1, node2, label = "Predaje", color = "red")
graph.add_edge(edge1)
graph.write_png("primer2_graph.png")

#Zadatak
graph = Dot(graph_type = "digraph", rankdir = "BT")
graph.set_node_defaults(shape = "record")
teacher = Node("Teacher", label = "{Nastavnik|+ime:String \n+prezime:String|\n}")
course = Node("Course", label = "{Kurs|\n|\n}")
student = Node("Student", label = "{Student|\n|\n}")
lesson = Node("Lesson", label = "{Predavanja|\n|\n}")
tutorial = Node("Tutorial", label = "{Konsultacije|\n |\n}")
assessment = Node("Assessment", label = "{Ocenjivanje|\n|\n}")
coursework = Node("Coursework", label = "{Predispitne obaveze|\n|\n}")
exam = Node("Exam", label = "{Ispit|\n|\n }")

S = Subgraph(rank='same')
S.add_node(teacher)
S.add_node(student)
S.add_node(course)

graph.add_subgraph(S)

graph.add_node(lesson)
graph.add_node(tutorial)
graph.add_node(assessment)
graph.add_node(coursework)
graph.add_node(exam)

graph.write_png("objektni_primer.png");
edge1 = Edge(teacher, course, label = "Predaje", arrowhead = "none", 
             arrowtail = "normal", headlabel = "1", taillabel = "1")
edge2 = Edge(student, course, label = "Pohađa",  arrowhead="none",
         arrowtail="normal",headlabel="1",taillabel="1")
edge3 = Edge(lesson, course, arrowhead="diamond",arrowtail="normal")
edge4 = Edge(tutorial, course, arrowhead="diamond",arrowtail="normal")
edge5 = Edge(assessment, course, arrowhead="diamond",arrowtail="normal")
edge6 = Edge(coursework, assessment, arrowhead="onormal")
edge7 = Edge(exam, assessment, arrowhead="onormal")
graph.add_edge(edge1)
graph.add_edge(edge2)
graph.add_edge(edge3)
graph.add_edge(edge4)
graph.add_edge(edge5)
graph.add_edge(edge6)
graph.add_edge(edge7)

graph.write_png("objektni_primer.png")

import codecs
with codecs.open("primer.dot", "w", "utf-8") as file:
    file.write(graph.to_string())
    
