import json
from tqdm import tqdm
import ast
import random
import copy 
import astor
import subprocess
import os



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
                    # Check if the assignment target is a tuple (multiple targets)
                    if isinstance(body_node.targets[0], ast.Tuple):
                        # Iterate over all targets in the tuple
                        for target in body_node.targets[0].elts:
                            if isinstance(target, ast.Name):
                                target_name = target.id
                                new_node = ast.Expr(value=ast.Name(id=target_name, ctx=ast.Load()))
                                node.body.insert(0, new_node)
                    elif isinstance(body_node.targets[0], ast.Name):
                        target_name = body_node.targets[0].id
                        new_node = ast.Expr(value=ast.Name(id=target_name, ctx=ast.Load()))
                        node.body.insert(0, new_node)
                    break
    return tree

# def introduce_syntax_errors(tree):
#     """
#     Introduce random SyntaxError in the AST by modifying the structure, like altering the order of nodes.
#     """
#     for node in ast.walk(tree):
#         if isinstance(node, ast.Expr):
#             # Create an empty 'pass' node
#             pass_node = ast.Pass()
#             # Wrap the pass node in an Expr node (since we are replacing an Expr)
#             pass_expr = ast.Expr(value=pass_node)
#             # Replace the expression with a 'pass' expression to simulate a SyntaxError
#             node.value = pass_expr
#             break
#     return tree

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


def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data

def inject_error(code):
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
    
    return code_with_name_error, code_with_unbound_local_error, code_with_syntax_error

def fetch_complier_feedback(in_code):
    try:
        completed_process = subprocess.run(['python', '-c', in_code], 
                                            capture_output=True, text=True, timeout=30)
        if completed_process.returncode == 0:  # No error
            tmp = completed_process.stdout.splitlines()
        else:  # Error occurred
            tmp = "Error: " + completed_process.stderr
    except subprocess.TimeoutExpired:
        tmp = "Time Out"

    except Exception as e:
        tmp = "Error: {}".format(str(e))

    return tmp
    

def inject_error_for_all_data(in_file, out_file):
    all_data = load_json_file(in_file, return_dict=True)
    all_codes_data = []
    for line in tqdm(all_data):
        orignal_code = line["code"]
        try:
            code_with_name_error, code_with_unbound_local_error, code_with_syntax_error = inject_error(orignal_code)
        
            name_error = fetch_complier_feedback(code_with_name_error)
            unbound_local_error = fetch_complier_feedback(code_with_unbound_local_error)
            syntax_error = fetch_complier_feedback(code_with_syntax_error)
            # print(name_error)
            # print(unbound_local_error)
            # print(syntax_error)
            name_error_dict = {
                "error_type": "name_error",
                "error_code": code_with_name_error, 
                "feedback": name_error,
                "question": line["question"],
                "code": line["code"],
                "answer": line["answer"]
            }
            
            unbound_local_error_dict = {
                "error_type": "unbound_local_error",
                "error_code": code_with_unbound_local_error, 
                "feedback": unbound_local_error,
                "question": line["question"],
                "code": line["code"],
                "answer": line["answer"]
            }
            
            syntax_error_dict = {
                "error_type": "syntax_error",
                "error_code": code_with_syntax_error, 
                "feedback": syntax_error,
                "question": line["question"],
                "code": line["code"],
                "answer": line["answer"]
            }
            
            all_codes_data.extend([
                name_error_dict, 
                unbound_local_error_dict, 
                syntax_error_dict
            ])
            # all_codes_data.append(name_error_dict)
            # all_codes_data.append(unbound_local_error_dict)
            # all_codes_data.append(syntax_error_dict)
            
        except Exception as e:  # 捕获任何异常并打印
            print(f"Error processing code: {e}")
            continue  # 继续处理下一个代码块
    
    
    with open(out_file, "w") as f:
        for i in tqdm(all_codes_data):
            f.write(json.dumps(i) + "\n")


if __name__ == '__main__':
    source_datasets = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json"
    save_file = os.path.join("Extract_Refiner_Data/error_datatsets", "train.json")
    inject_error_for_all_data(source_datasets, save_file)
    