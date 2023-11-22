import ast
import matplotlib.pyplot as plt
import networkx as nx

def plot_ast(ast_node, graph, parent=None, pos=None, level=0, width=2, leaf_width=2):
    """
    递归遍历 AST，将节点添加到图中，并为它们分配位置。
    """
    if pos is None:
        pos = {}

    # 节点标识
    node_id = id(ast_node)

    # 节点标签
    node_label = f"{type(ast_node).__name__}\n({level})"
    
    # 位置分配（水平位置依赖于节点在其层级中的顺序，垂直位置依赖于层级）
    if parent is None:  # 根节点
        pos[node_id] = (0, -level*width)
    else:
        parent_id = id(parent)
        siblings = list(ast.iter_child_nodes(parent))
        index = siblings.index(ast_node)
        if len(siblings) > 1:
            # 对于有多个孩子的节点，调整位置以避免重叠
            pos[node_id] = (pos[parent_id][0] + (index - (len(siblings) - 1) / 2) * leaf_width, -level*width)
        else:
            # 单个孩子直接继承父节点位置
            pos[node_id] = (pos[parent_id][0], -level*width)

    graph.add_node(node_id, label=node_label)

    if parent is not None:
        graph.add_edge(id(parent), node_id)

    for child in ast.iter_child_nodes(ast_node):
        plot_ast(child, graph, ast_node, pos, level+1, width, leaf_width)

    return pos

# 提供的 Python 代码
code = """
def solution():
    movie_c_length = 1.25 * 60
    movie_b_length = movie_c_length + 5
    movie_a_length = movie_b_length / 4
    result = movie_a_length
    return result

print(solution())
"""

# 解析代码
parsed_code = ast.parse(code)
print(ast.dump(parsed_code, indent=4))
# # 创建图形
# ast_graph = nx.DiGraph()
# pos = plot_ast(parsed_code, ast_graph)

# # 绘制 AST 图形
# plt.figure(figsize=(12, 8))
# nx.draw(ast_graph, pos, labels=nx.get_node_attributes(ast_graph, 'label'), with_labels=True, arrows=False)
# plt.title("AST of the provided Python code")
# plt.show()
