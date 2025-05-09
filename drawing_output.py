import matplotlib.pyplot as plt

def drawing_output(times, eum, rk, output_thing):
    plt.figure()
    plt.plot(times, eum, label='Euler', linestyle='--')
    plt.plot(times, rk, label='RK4', linestyle='-')
    plt.xlabel("Time [s]")

    if output_thing == "phi":
        plt.ylabel("Position φ [rad]")
        plt.title("Comparison of methods: shaft J2 position")
    elif output_thing == "omega":
        plt.ylabel("Angular velocity ω [rad/s]")
        plt.title("Comparison of methods: shaft J2 angular velocity")

    plt.legend()
    plt.grid(True)
    
