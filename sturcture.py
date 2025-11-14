import os
import yaml

ROOT_FOLDER = r"P:\~Pi~Py\ml-py"
YAML_FILE = "structure.yaml"
README_FILE = "README.md"


# --------------------------------------------------------
# Read directory structure
# --------------------------------------------------------
def read_structure(root_path):
    structure = {}

    try:
        items = sorted(os.listdir(root_path))
    except PermissionError:
        print(f"Access denied: {root_path}")
        return structure

    for item in items:
        if item.startswith("."):
            continue
        path = os.path.join(root_path, item)
        if os.path.isdir(path):
            try:
                files = [
                    f for f in sorted(os.listdir(path))
                    if os.path.isfile(os.path.join(path, f))
                ]
            except PermissionError:
                files = []

            structure[item] = files

    return structure


# --------------------------------------------------------
# Write structure.yaml
# --------------------------------------------------------
def write_yaml(structure):
    data = {ROOT_FOLDER.split("\\")[-1]: structure}
    with open(YAML_FILE, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False)


# --------------------------------------------------------
# Create README.md in your EXACT format
# --------------------------------------------------------
def write_readme(yaml_content):

    content = f"""# **Machine Learning**

### **Directory Structure:**

```yaml
{yaml_content}
```
> <i>Rang me tere malang firu me laila!!</i>
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)
# --------------------------------------------------------
if __name__ == "__main__":
    structure = read_structure(ROOT_FOLDER)
    write_yaml(structure)

    with open(YAML_FILE, "r", encoding="utf-8") as f:
        yaml_content = f.read()

    write_readme(yaml_content)