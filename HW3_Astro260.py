import numpy as np
import pandas as pd

def value_det(a,z):
    """
    Determines value for a_5 in Nuclear Binding Energy EQ
    Input: a,z
    Output: 0 if a is odd, 12 if a & z are even, -12 if a is even and z is odd
    """
    if a%2 == 0:
        if z%2 == 0:
            return(12.0)
    if a%2 == 0:
        if z%2 !=0:
            return(-12.0)
    if a%2 != 0:
            return(0)
        
def Volume_term (a):
    """
    Defines the volume term of the semi-empirical mass formula
    Input: a
    Output: first term in equation
    """
    term1 = 15.8*a
    return term1

def Surface_term(a):
    """
    Defines the surface term of the semi-empirical mass formula
    Input: a
    Output: first term in equation
    """
    term2 = -18.3*(a**(2/3))
    return term2
def Coulomb_term(a, z):
    """
    Defines the Coulomb term of the semi-empirical mass formula
    Input: a , z
    Output: first term in equation
    """
    term3 = -0.714*(z**2/(a**(1/3)))
    return term3
def Asymmetry_term(a, z):
    """
    Defines the asymmetry term of the semi-empirical mass formula
    Input: a , z
    Output: first term in equation
    """
    term4 = -23.2*((a-2*z)**2/a)
    return term4
def Paring_term(a, z):
    """
    Defines the Paring term of the semi-empirical mass formula
    which also uses the value_det function to define a_5
    Input: a , z
    Output: first term in equation
    """
    term5 = value_det(a,z)/a**(1/2)
    return term5
def Per_nucleon(a,z):
    """
    Calculates the binding energy per nucleon, using the same formula as
    function Semi-emp_mass but divides again by the [a] variable
    Input: a , z
    Output Binding energy per nucleon for given atomic number and mass
    """
    value = ((Volume_term(a)+Surface_term(a)+Coulomb_term(a,z)+Asymmetry_term(a,z)+Paring_term(a,z))/a)
    return value
def Semi_emp_mass(a,z):
    """
    Semi-empirical Mass Formula for a given mass [a] and atomic number [z]
    uses the 5 term functions to accomplish it's function
    Input: a , z
    Output: Nuclear binding energy
    """
    value = (Volume_term(a)+Surface_term(a)+Coulomb_term(a,z)+Asymmetry_term(a,z)+Paring_term(a,z))
    return value
print('\n')
print('Part A: for binding energy A = 58 and Z = 28')
part1answer = Semi_emp_mass(58,28)
print('NBE for these values is ',part1answer)
print('\n')
print('Part B: The binding energy per nucleuon is ',Per_nucleon(58,28))
print('\n')
print('Part C: Please enter an atomic number value [Z]: ')

x = (input())
initialvalue = np.int(x)


def PartCfunction(z):
    """Takes a given value of z and calculates Sem_emp_mass and Per_nucleon functions
    for the input z to 3 * z.
    Input: a , z
    Output: Max values for atomic mass and binding energy per nucleon
    """
    maxvalue = 0
    maxPernucleon = 0
    maxrange = z * 3
    for x in range(maxrange):#runs both functions for full length z*3
        answerSEM = Semi_emp_mass(x+1,z)
        answerPERnucleon = Per_nucleon(x+1,z)
        
        if answerSEM > maxvalue:#both if statements finds the max value of the repective function
            maxvalue = answerSEM
        if answerPERnucleon > maxPernucleon:
            maxPernucleon = answerPERnucleon
            a = maxvalue / maxPernucleon#calculates atomic mass
    return a , maxPernucleon
    
C = PartCfunction(initialvalue)
print('The mass number and corresponding binding energy most stable is', C)
print('\n')

print('Part D: for [Z] from 1 to 100, the most stable value for A, and corresponding binding energy per nucleon is:')
for i in range(100):
    i = np.int(i)
    listforD = []
    D = PartCfunction(i + 1)
    listforD.append(D)
    print(listforD)

#attempts at E as comments  
#print('Part E: Data plotting for experimental data and nuclear data text file:')
#expdata = np.savetxt('SMF',listforD,delimiter = ',')

#opendatafie = np.loadtxt('C:\PythonFiles\nuclear_data.txt',skiprows = 1)










 






