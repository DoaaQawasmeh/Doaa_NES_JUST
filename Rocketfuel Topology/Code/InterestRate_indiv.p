set xrange [0:85]
set yrange [0:850]
set xlabel "Time"
set ylabel "Interest Rate(packets/s)"
set terminal png 
set output 'final_curves/InterestRateWithoutSolution.png'
plot "curves/bb-469_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-469-CIFA-ATTACK',"curves/bb-483_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-483-CIFA-ATTACK',"curves/bb-627_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-627-CIFA-ATTACK',"curves/gw-423_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router gw-423-CIFA-ATTACK'
set output 'final_curves/InterestRateWithSolution.png'
plot "curves/bb-469_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-469-MitigationSolution',"curves/bb-483_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-483-MitigationSolution',"curves/bb-627_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-627-MitigationSolution',"curves/gw-423_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router gw-423-MitigationSolution'
