GHG Renamer
===========

A Python tool to rename various names used for Greenhouse Gas emissions or
concentrations tables to a common naming scheme.

Example:

```python
from ghgrenamer import to_shortname

to_shortname("CO2_emissions")  # => 'CO2'

```

Example usage:

```python
from ghgrenamer import to_shortname

import pandas as pd

df = pd.read_excel(
    "Supplementary_Table_UoM_GHGConcentrations-1-1-0_annualmeans_v23March2017.xls",
    skiprows=21,
    index_col=0,
    sheet_name=1
)

print([to_shortname(i) for i in df.columns])
"""
['CO2', 'CH4', 'N2O', 'HFC-134a', 'HFC-23', 'HFC-32', 'HFC-125', 'HFC-143a', 'HFC-152a', 'HFC-227ea', 'HFC-236fa', 'HFC-245fa', 'HFC-365mfc', 'HFC-43-10mee', 'NF3',  # ...
"""
```

Alternative names are defined in `names.yaml`.
Run `make` to update them into the `mappings.py` submodule.
