import matplotlib.pyplot as plt
import lightkurve as lk
import base64
from io import BytesIO
import numpy as np


def main():
    # Generate some sample data (replace this with your actual data)
    time = np.linspace(0, 10, 100)
    flux = np.sin(time)

    # Create a new figure
    fig = plt.figure()

    # Plot the data
    plt.plot(time, flux)
    plt.xlabel("Time (days)")
    plt.ylabel("Flux")
    plt.title("Light Curve")

    # Save the plot to a PNG file
    plot_bytes = convert_plot_to_bytes(fig)
    with open("./KIC8462852.png", "wb") as fh:
        fh.write(plot_bytes)
    """
    lc = lk.search_lightcurve(target="KIC 8462852", mission="Kepler").download().PDCSAP_FLUX
    fig = plt.figure()
    lc.plot()
    plt.xlabel("Time (days)")
    plt.ylabel("Flux")
    plt.title("Light Curve")
    # plt.show()  # Display the plot
    plot_bytes = convert_plot_to_bytes(fig)
    with open("KIC8462852.png", "wb") as fh:
        fh.write(plot_bytes)
    """


def convert_plot_to_bytes(fig) -> bytes:
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)
    return buffer.getvalue()


if __name__ == "__main__":
    main()