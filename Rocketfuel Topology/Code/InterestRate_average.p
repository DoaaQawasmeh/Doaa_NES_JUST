set xrange [0:85]
set yrange [0:85]
set xlabel "Time"
set ylabel "Interest Rate(packets/s)"
set terminal png 
set output 'final_curves/AverageInterestRateWithoutSolution.png'
plot "curves/average/AverageInterestRate_use_0_Final.txt" using 1:2 w lp title 'Interest Rate for good-consumers-CIFA-ATTACK'
set output 'final_curves/AverageInterestRateWithSolution.png'
plot "curves/average/AverageInterestRate_use_1_Final.txt" using 1:2 w lp title 'Interest Rate for good-consumers-MitigationSolution'
