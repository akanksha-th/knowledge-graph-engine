from pyvis.network import Network
from api.schema.graph import Triple

def generate_graph(triples: list[Triple]) -> str:
    net = Network(height="750px", width="100%", directed=True)
    
    for triple in triples:
        net.add_node(triple.subject, label=triple.subject, color="lightblue")
        net.add_node(triple.obj, label=triple.obj, color="lightgreen")
        net.add_edge(triple.subject, triple.obj, label=triple.predicate, color="gray")
    
    return net.generate_html()



if __name__ == "__main__":
    kg = [
    {"subject": "We", "predicate": "have", "object": "purple candles"},
    {"subject": "We", "predicate": "have", "object": "purple candles in our wreath"},
    {"subject": "purple candles in our wreath", "predicate": "consists_of", "object": "purple candles"},
    {"subject": "purple candles in our wreath", "predicate": "is_a_component_of", "object": "wreath"},
    {"subject": "purple candles in our wreath", "predicate": "is_of_type", "object": "candles"},
    {"subject": "purple", "predicate": "is", "object": "the new Red"},
    {"subject": "traffic light", "predicate": "signals", "object": "STOP"},
    {"subject": "traffic light", "predicate": "signals", "object": "wait"},
    {"subject": "traffic light", "predicate": "signals (indicates)", "object": "pay attention"}
    ]
    
    print(generate_graph(kg))