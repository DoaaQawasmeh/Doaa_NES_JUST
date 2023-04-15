set xrange [0:85]
set yrange [-0.5:1.5]
set xlabel "Time"
set xzeroaxis
set ylabel "PIT Utilization Rate"
set terminal png 
set output 'final_curves/UtilizationRateWithout.png'
plot "curves/bb-2_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(bb2)',"curves/bb-3_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(bb3)',"curves/bb-5_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(bb5)',"curves/gw-3_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(gw3)'
set output 'final_curves/UtilizationRateWith.png'
plot "curves/bb-2_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(bb2)',"curves/bb-3_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(bb3)',"curves/bb-5_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(bb5)',"curves/gw-3_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(gw3)'
