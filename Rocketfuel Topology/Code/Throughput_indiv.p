set xrange [0:85]
set yrange [-1:8000]
set xlabel "Time"
set xzeroaxis
set ylabel "Throughput (kb/s)"
set terminal png 
set output 'final_curves/ThroughputWithoutSolution.png'
plot "curves/bb-469_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router bb-469-CIFA-ATTACK',"curves/bb-483_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router bb-483-CIFA-ATTACK',"curves/bb-627_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router bb-627-CIFA-ATTACK',"curves/gw-423_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router gw-423-CIFA-ATTACK'
set output 'final_curves/ThroughputWithSolution.png'
plot "curves/bb-469_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router bb-469-MitigationSolution',"curves/bb-483_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router bb-483-MitigationSolution',"curves/bb-627_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router bb-627-MitigationSolution',"curves/gw-423_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router gw-423-MitigationSolution'
