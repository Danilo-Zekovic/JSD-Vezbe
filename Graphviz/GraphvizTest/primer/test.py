'''
Created on Dec 20, 2014

'''
import pydot
i = "2"
graph = pydot.graph_from_dot_file("primer" + i + ".dot")
graph.write_png("primer" + i + ".png")