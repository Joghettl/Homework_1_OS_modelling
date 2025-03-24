# %% [markdown]
# # Profitability of a single PV system

# %%

#functions
def calculate_price_n_return(p_supply,p_grid_var, p_grid_fixed, r_sales, grid_purchase):
    """
    The aim of this function is to calculate the annuitys for the electricity price and the return (profits) from the PV-system
    """
    p=(grid_purchase*p_supply)+(grid_purchase*p_grid_var)+p_grid_fixed
    if(grid_purchase==grid_a): r= overproduction_a*r_sales
    elif(grid_purchase==load_a):r=generation_a*r_sales
    else: r=0.0
    return p, r


def calculation_interestrate(Matrikelnummer): 
    """
    This function determines the interest rate dependent on the 'Matrikelnummer'.  
    """
    q = sum(int(digit) for digit in str(Matrikelnummer))
    a=((q * 5) % 40) * 10**-2
    if(a>0.1):
        a=0.05
    elif(a < 0.001): a=0.001
    return a

# NPV for the PV-system
def calculate_npv(p_invest, life_t, p, r, interest_r):
    """
    This function calculates the net present value for the whole household in terms of electricity.
    """
    npv_1 = -p_invest  

    for t in range (1, life_t + 1):
        npv_1 -= (p)/(1+interest_r)**t
        npv_1 += r/(1+interest_r)**t
    return npv_1

MatrNr = 12012289
interest_rate = calculation_interestrate(MatrNr)


C_installed = 3 #kWp
P_invest_spec = 800 #€/kWp
lifetime = 25 #years
P_invest = P_invest_spec*C_installed

#electricity purchase and sale
P_supply = 0.2 # €/kWh
P_grid_var = 0.05 # €/kWh
P_grid_fixed = 100 # €/a
R_sales = 0.1 #€/kWh

#profiles
load_d = 5*0.5+1+1.5*3+2*2+3*2+2.5*2+2+1.5*2+2*2+1.5+0.5*3 #kWh
load_a = load_d*365
generation_d = 0.5*2+2+2.5*2+3*2+2.5*2+2+1.5+0.5 #kWh
generation_a = generation_d*365
grid_d = 0.5*5+1+1.5+2*1+0.5+1.5+2+1.5+3*0.5 #kWh
grid_a = grid_d*365
overproduction_d = 0.5+0.5+0.5+0.5 #kWh
overproduction_a = overproduction_d*365



# %% [markdown]
# ## a) Net Present Value

# %%
P_1 = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, R_sales, grid_a)[0]
R_1 = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, R_sales, grid_a)[1]
npv_1 = calculate_npv(P_invest,lifetime,P_1, R_1, interest_rate)





# %% [markdown]
# NPV for purchase only

# %%


P_2 = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, 0, load_a)[0]
R_2 = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, 0, load_a)[1]

P_2a = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, R_sales, load_a)[0]
R_2a = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, R_sales, load_a)[1]

npv_2 = calculate_npv(0.0, lifetime, P_2, R_2, interest_rate)
npv_2a = calculate_npv(P_invest, lifetime, P_2a, R_2a, interest_rate)



# %% [markdown]

# NPV with no remuneration for surplus feedin

# %%

P_3 = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, 0, grid_a)[0]
R_3 = calculate_price_n_return(P_supply,P_grid_var,P_grid_fixed, 0, grid_a)[1]
npv_3 = calculate_npv(P_invest, lifetime, P_3, R_3, interest_rate)


print("Net Present Value over the entire technical lifetime of the PV system is",round(npv_1,2))
print("Net Present Value from pure electricity purchase with no pv installed is",round(npv_2,2))
print("Net Present Value from pure electricity purchase with pv installed is",round(npv_2a,2))
print("Net Present Value if there is no remuneration for surplus feed-in is",round(npv_3,2))

