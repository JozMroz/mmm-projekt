import matplotlib.pyplot as plt

def drawing_input(x, y, signal_type, ylabel='Input [-]'):
    plt.plot(x, y)
    plt.xlabel('Time [s]')
    plt.ylabel(ylabel)

    if signal_type == 'sinus':
        plt.title('Sinus function')
    elif signal_type == 'triangle':
        plt.title('Triangle function')
    elif signal_type == 'rect':
        plt.title('Rectangular function')
    elif signal_type == 'rect_imp':
        plt.title('Rectangular impulse function')
    elif signal_type == 'trian_imp':
        plt.title('Triangular impulse function')
    else:
        plt.title('System Response')
    plt.show()
