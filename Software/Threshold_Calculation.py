import numpy as np
s = np.random.normal(0,10,1000)
s_mean = np.mean(abs(s))
Loop_Factor = np.arange(0,3,0.1)
Max_Array = [0]
for J in Loop_Factor:
    for K in Loop_Factor:
        for L in Loop_Factor:
            if L > K and K > J:
                num_1 = 0
                num_2 = 0
                num_3 = 0
                w_1 = 0
                w_2 = 0
                w_3 = 0
                threshold_1 = J*s_mean
                threshold_2 = K*s_mean
                threshold_3 = L*s_mean
                for w in s:
                    
                    if abs(w) > threshold_1 and abs(w) < threshold_2:
                        num_1 = num_1 + 1
                        w_1 = w_1 + abs(w)
                    if abs(w) > threshold_2 and abs(w) < threshold_3:
                        num_2 = num_2 + 1
                        w_2 = w_2 + abs(w)
                    if abs(w) > threshold_3:
                        num_3 = num_3 + 1
                        w_3 = w_3 + abs(w)
                
                print("J:",J,"K:",K,"L:",L)
                print("num_1:",num_1,"num_2:",num_2,"num_3:",num_3)
                print("w_1:",w_1,"w_2:",w_2,"w_3:",w_3)
                max = ((w_1 + 2*w_2 + 3*w_3)**2)/(num_1+4*num_2+9*num_3)
                print(max)
                Max_Array.append(max);

Max_Array
T=np.max(Max_Array)
print(T)