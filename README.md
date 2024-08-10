# chem_eq_balancer
Balancing chemical equations in Python
Parses the inputs then balances the equations using matrices. 
Each row represents an element and each column represents a compound
The matrix is then transposed and the nullspace of the matrix is computed to get the coefficients of the equation.
The nullspace is the set of all vectors that multiply the matrix to produce a vector of zeros. In this case, the nullspace corresponds to the coefficients of the balanced equation. The solution is then scaled to ensure that all coefficients are integers.
Output can be found in terminal (no new blocks/windows). Takes your inputs/equations in a intuitive and simple manner.
