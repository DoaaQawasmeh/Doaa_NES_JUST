set xrange [0:85]
set yrange [0:850]
set xlabel "Time"
set ylabel "Interest Rate(packets/s)"
set terminal png 
set output 'final_curves/InterestRateWithoutSolution.png'
plot "curves/bb-2_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-2-CIFA-ATTACK',"curves/bb-3_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-3-CIFA-ATTACK',"curves/bb-5_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-5-CIFA-ATTACK',"curves/gw-3_InterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for router gw-3-CIFA-ATTACK'
set output 'final_curves/InterestRateWithSolution.png'
plot "curves/bb-2_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-2-MitigationSolution',"curves/bb-3_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-3-MitigationSolution',"curves/bb-5_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router bb-5-MitigationSolution',"curves/gw-3_InterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for router gw-3-MitigationSolution'
