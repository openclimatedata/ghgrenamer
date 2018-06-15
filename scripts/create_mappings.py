import yaml

from pprint import pformat
from pathlib import Path

root = Path(__file__).parents[1]


with open(root / "names.yaml") as f:
    data = yaml.load(f)

mappings = {}
for key, names in data.items():
    for name in names:
        mappings[name.lower()] = key
    mappings[key.lower()] = key

with open(root / "ghgrenamer/mappings.py", "w") as outfile:
    outfile.write(
        "mappings = {\n " +
        pformat(mappings, indent=4)[1:-1] +
        "\n}")

