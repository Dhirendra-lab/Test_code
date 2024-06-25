import ast
import os
import sys
from stdlib_list import stdlib_list

def get_top_level_imports(filepath):
    with open(filepath, "r") as file:
        tree = ast.parse(file.read(), filename=filepath)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top_level_module = alias.name.split(".")[0]
                imports.add(top_level_module)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                top_level_module = node.module.split(".")[0]
                imports.add(top_level_module)
    return imports

def main():
    stdlib_modules = set(stdlib_list(f"{sys.version_info.major}.{sys.version_info.minor}"))

    with open("requirements.txt", "r") as file:
        requirements = {line.split("==")[0].strip() for line in file.readlines()}

    missing_imports = set()
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                imports = get_top_level_imports(filepath)
                missing = imports - requirements - stdlib_modules
                if missing:
                    print(f"Missing imports in requirements.txt: {missing} in {filepath}")
                    missing_imports.update(missing)

    if missing_imports:
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
