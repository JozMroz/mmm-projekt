import matplotlib.pyplot as plt

def drawing_plot(x, y, signal_type, ylabel='Output [-]'):
    plt.plot(x, y)
    plt.xlabel('Time [s]')
    plt.ylabel(ylabel)

    if signal_type == 'fun.sin_Tm':
        plt.title('Response to Sinus Input')
    elif signal_type == 'triangle':
        plt.title('Response to Triangle Input')
    elif signal_type == 'sinus':
        plt.title('Response to Sinusoidal Input')
    else:
        plt.title('System Response')
    plt.show()