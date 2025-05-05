import matplotlib.pyplot as plt
import function_gen

A=1
f=1
dt=0.01
tk=5
#wywołanie sin
t, Tm = function_gen.sin_Tm(A,f, dt, tk)
#plot sin
plt.subplot(1,5,1)
plt.plot(t,Tm)
#wywołanie rec okresowe
t, Tm = function_gen.rec_Tm(A,f, dt, tk)
#plot rec okresowe
plt.subplot(1,5,2)
plt.plot(t,Tm)
#wywołanie trian okresowe
t, Tm = function_gen.trian_Tm(A,f, dt, tk)
#plot trian okresowe
plt.subplot(1,5,3)
plt.plot(t,Tm)
#wywołanie rec impuls
t, Tm = function_gen.rec_imp_Tm(A, dt, tk)
#plot rec impuls
plt.subplot(1,5,4)
plt.plot(t,Tm)
#wywołanie trian impuls
t, Tm = function_gen.trian_imp_Tm(A, dt, tk)
#plot trian impuls
plt.subplot(1,5,5)
plt.plot(t,Tm)
plt.show()
