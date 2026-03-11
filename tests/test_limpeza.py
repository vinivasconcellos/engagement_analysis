import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))
from automation_lib.limpeza_dados import converter_k

def converter_k_com_nada():
    assert converter_k("") == 0

def test_converter_k_com_traco():
    assert converter_k("-") == 0