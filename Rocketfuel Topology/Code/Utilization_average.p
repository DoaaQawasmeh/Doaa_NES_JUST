set xrange [0:85]
set yrange [-0.5:1.5]
set xlabel "Time"
set ytic 0.1
set xzeroaxis
set ylabel "PIT Utilization Rate"
set terminal png 
set output 'final_curves/AverageUtilizationRateWithoutSolution.png'
plot "curves/average/AverageUtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate for good-consumers-CIFA-ATTACK'
set output 'final_curves/AverageUtilizationRateWithSolution.png'
plot "curves/average/AverageUtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate for good-consumers-MitigationSolution'
