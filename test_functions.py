import matplotlib.pyplot as plt
import function_gen

A=1
f=1

#wywołanie sin
t, Tm = function_gen.sin_Tm(A,f)
#plot sin
plt.subplot(1,5,1)
plt.plot(t,Tm)
#wywołanie rec okresowe
t, Tm = function_gen.rec_Tm(A,f)
#plot rec okresowe
plt.subplot(1,5,2)
plt.plot(t,Tm)
#wywołanie trian okresowe
t, Tm = function_gen.trian_Tm(A,f)
#plot trian okresowe
plt.subplot(1,5,3)
plt.plot(t,Tm)
#wywołanie rec impuls
t, Tm = function_gen.rec_imp_Tm(A)
#plot rec impuls
plt.subplot(1,5,4)
plt.plot(t,Tm)
#wywołanie trian impuls
t, Tm = function_gen.trian_imp_Tm(A)
#plot trian impuls
plt.subplot(1,5,5)
plt.plot(t,Tm)
plt.show()