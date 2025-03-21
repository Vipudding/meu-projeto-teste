import pytest
from cadastro import validar_cep

@pytest.mark.parametrize("cep, cidade, esperado", [
    ("18050100", "Sorocaba", True),
    ("18195000", "Capela do Alto", True),
    ("18130020", "São Roque", True),
    ("19000000", "Votorantim", False),  
    ("18125000", "Alumínio", True),
    ("18560000", "Iperó", True),
    ("18147000", "Araçariguama", True),
    ("18190000", "Araçoiaba da Serra", True),
    ("13300000", "Itu", True),
    ("18120000", "Mairinque", True),
    ("13315000", "Cabreúva", True),
    ("18195000", "Capela do Alto", True),
    ("13320000", "Salto", True),
    ("18160000", "Salto de Pirapora", True),
    ("18130000", "São Roque", True),
    ("18225000", "Sarapuí", True),
    ("18000000", "Sorocaba", True),
    ("18110000", "Votorantim", True),
    ("18540000", "Porto Feliz", True),
])
def test_validar_cep(cep, cidade, esperado):
    assert validar_cep(cep, cidade) == esperado