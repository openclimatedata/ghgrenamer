import pandas as pd

from ghgrenamer import mappings
from ghgrenamer import to_shortname

from pathlib import Path

root = Path(__file__).parents[1]

magicc_rcp = pd.read_csv(
    root / "tests/examples/RCP26.SCEN",
    delimiter=r"\s+",
    skiprows=7,
    nrows=41,
    header=0,
    index_col=0
)

hector_rcp = pd.read_csv(
    root / "tests/examples/RCP26_emissions.csv",
    index_col=0,
    comment=";")

def test_magicc_rcp():
    for name in magicc_rcp.columns:
        print(name)
        assert to_shortname(name) in mappings.values()

def test_hector_rcp():
    for name in hector_rcp.columns:
        print(name)
        assert to_shortname(name) in mappings.values()

def test_not_found():
    assert to_shortname("CO2-special") == "CO2-special"

def test_space():
    assert to_shortname("Halon 1211") == "Halon-1211"

def test_lowercase():
    assert to_shortname("halon-1211") == "Halon-1211"

def test_subscript():
    assert to_shortname("CO₂") == "CO2"
