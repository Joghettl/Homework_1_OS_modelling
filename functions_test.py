import pytest
import Profitabilty_PV_system as HW2

def test_calculate_price_n_return():
    p_supply= 0.3
    p_grid_var= 0.05
    p_grid_fixed= 84.0
    r_sales= 0.1
    grid_purchase= 0.5

    pnr = HW2.calculate_price_n_return(p_supply,p_grid_var, p_grid_fixed, r_sales, grid_purchase)
    assert isinstance(pnr, tuple),'pnr should be tuple'
    assert isinstance(pnr[0], float),'pnr[0] should be float'
    assert isinstance(pnr[1], float),'pnr[1] should be float'

def test_calculate_interestrate():
    Matrikelnummer = 12133389
    interest_rate = HW2.calculation_interestrate(Matrikelnummer)
    assert isinstance(interest_rate, float),'interest_rate should be float'
    if(interest_rate>0.1): raise ValueError('interest_rate out of range')


test_calculate_price_n_return()
test_calculate_interestrate()