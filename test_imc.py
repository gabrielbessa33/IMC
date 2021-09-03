import pytest
from imc import cal_imc, num_neg

#Calculo de IMCs diferentes
@pytest.mark.parametrize('a,b,expected', [(84, 1.80, 25.93), (70,1.50,31.11), (75,1.77,23.94), (72, 1.64,26.77), (65, 1.50, 28.89)])
def test_calc(a,b, expected):
    assert cal_imc(a,b) == expected
#Calculo de diferentes IMCs incluindo um que seja com o valor negativo
@pytest.mark.parametrize('a,expected', [(70, 1.45, 33.29), (71,1.69,24.86), (-74,1.65,False)])
def test_negativ(a,b,expected):
    assert num_neg(a,b) == expected
