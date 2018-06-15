GHG Renamer
===========

A Python tool to rename various names used for Greenhouse Gas emissions or
concentrations tables to a common naming scheme.

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
 ['CO2',
  'CH4',
  'N2O',
  'HFC134a',
  'HFC23',
  'HFC32',
  'HFC125',
  'HFC143A',
  'HFC152A',
  'HFC227EA',
  'HFC236FA',
  'HFC245fa',
  'HFC-365mfc',
  'HFC-43-10mee',
  'NF3',
  'SF6',
  # ...
"""
```

Alternative names are defined in `names.yaml`.
Run `make` to update them into the `mappings.py` submodule.
