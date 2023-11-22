import ast
import random
import copy 
import astor

def randomly_rename_variables(tree):
    """
    Rename variables in the AST to introduce NameError by changing their names to something random.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            node.id = 'undefined_var_' + str(random.randint(0, 9999))
    return tree

def randomly_reference_before_assignment(tree):
    """
    Reference variables before assignment in the AST to introduce UnboundLocalError.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for body_node in node.body:
                if isinstance(body_node, ast.Assign):
                    target_name = body_node.targets[0].id
                    new_node = ast.Expr(value=ast.Name(id=target_name, ctx=ast.Load()))
                    node.body.insert(0, new_node)
                    break
    return tree

# def introduce_syntax_errors(tree):
#     """
#     Introduce a guaranteed SyntaxError in the AST by manipulating the structure in various ways.
#     """
#     error_methods = [
#         lambda node: setattr(node, 'name', '1invalid'),  # Invalid function name (starts with a number)
#         lambda node: node.body.insert(0, ast.For()),  # Insert incomplete 'for' statement
#         lambda node: node.body.append(ast.Pass()) if node.body else node.body.insert(0, ast.Pass()),  # Append 'pass' in an incorrect location
#         lambda node: node.body.insert(0, ast.Return(value=ast.Name(id='x', ctx=ast.Load()))),  # Insert 'return' at the start of the body
#         lambda node: setattr(node, 'body', [ast.Break()])  # Replace the function body with 'break'
#     ]

#     # Apply an error method to the first FunctionDef found
#     for node in ast.walk(tree):
#         if isinstance(node, ast.FunctionDef):
#             random.choice(error_methods)(node)
#             break  # Apply only one error to ensure it's a SyntaxError

    # return tree

def introduce_syntax_errors(tree):
    """
    Introduce a guaranteed SyntaxError in the AST by adding an additional
    return statement at the beginning of the function definition.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Insert a return statement at the beginning of the function body
            return_node = ast.Return(value=ast.Str(s='Syntax Error'))
            node.body.insert(0, return_node)
            break
    return tree


def run_code_and_check_errors(code):
    try:
        # Run the Python code using exec()
        exec_locals = {}
        exec(code, None, exec_locals)
    except Exception as e:
        # If there's an error, print it
        print(f"Error: {e}")
    else:
        # If there's no error, print the result of the function
        if 'solution' in exec_locals:
            print(f"Function Output: {exec_locals['solution']()}")
        else:
            print("No solution function found.")

# Sample Python code
code = """
def solution():
    movie_c_length = 1.25 * 60
    movie_b_length = movie_c_length + 5
    movie_a_length = movie_b_length / 4
    result = movie_a_length
    return result

print(solution())
"""

# Parse the code into an AST
tree = ast.parse(code)

# Apply transformations to introduce errors
tree_with_name_error = randomly_rename_variables(copy.deepcopy(tree))
tree_with_unbound_local_error = randomly_reference_before_assignment(copy.deepcopy(tree))
tree_with_syntax_error = introduce_syntax_errors(copy.deepcopy(tree))

# Serialize the modified ASTs back to source code (optional step)
code_with_name_error = astor.to_source(tree_with_name_error)
code_with_unbound_local_error = astor.to_source(tree_with_unbound_local_error)
code_with_syntax_error = astor.to_source(tree_with_syntax_error)

# Check each modified code for errors
print("Checking for NameError:")
run_code_and_check_errors(code_with_name_error)

print("\nChecking for UnboundLocalError:")
run_code_and_check_errors(code_with_unbound_local_error)

print("\nChecking for SyntaxError:")
run_code_and_check_errors(code_with_syntax_error)