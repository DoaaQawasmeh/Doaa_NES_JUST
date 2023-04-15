set xrange [0:85]
set yrange [-0.5:1.5]
set xlabel "Time"
set xzeroaxis
set ylabel "PIT Utilization Rate"
set terminal png 
set output 'final_curves/UtilizationRateWithout.png'
plot "curves/bb-469_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(bb-469)',"curves/bb-483_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(bb483)',"curves/bb-627_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(bb-627)',"curves/gw-423_UtilizationRate_use_0_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-CIFA-ATTACK(gw-423)'
set output 'final_curves/UtilizationRateWith.png'
plot "curves/bb-469_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(bb-469)',"curves/bb-483_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(bb-483)',"curves/bb-627_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(bb-627)',"curves/gw-423_UtilizationRate_use_1_Final.txt" using 1:2 w lp title 'PIT Utilization Rate-MitigationSolution(gw-423)'
