def build_conflict_graph(requests):
    n = len(requests)
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            c1, c2 = requests[i], requests[j]
            if c1["group"] == c2["group"] or c1["professor"] == c2["professor"]:
                graph[i].append(j)
                graph[j].append(i)
    return graph
def welsh_powell_coloring(graph):
    sorted_nodes = sorted(graph.keys(), key=lambda k: len(graph[k]), reverse=True)
    coloring = {}
    current_color = 0
    while sorted_nodes:
        uncolored = []
        colored_in_pass = set()
        for node in sorted_nodes:
            if not any(n in colored_in_pass for n in graph[node]):
                coloring[node] = current_color
                colored_in_pass.add(node)
            else:
                uncolored.append(node)  
        sorted_nodes = uncolored
        current_color += 1
    return coloring
def graph_schedule(requests, teaching_config):
    slots = [(d, s) for d in teaching_config["days"] for s in teaching_config["standard_slots"]]
    graph = build_conflict_graph(requests)
    coloring = welsh_powell_coloring(graph)
    for idx, color in coloring.items():
        if color < len(slots):
            d, s = slots[color]
            requests[idx]["day"] = d
            requests[idx]["slot"] = s
    return requests