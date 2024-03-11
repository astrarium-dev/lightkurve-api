from src.lkutils import conversions
import matplotlib.pyplot as plt
import lightkurve as lk


def test_base64_plot_conversion():
    """
    dummy test to fill in while setting up automated testing
    """
    lc = lk.search_lightcurve(target="KIC 8462852", mission="Kepler").download().PDCSAP_FLUX
    lc.plot()
    plt.xlabel("Time (days)")
    plt.ylabel("Flux")
    plt.title("Light Curve")
    base64_image = conversions.convert_plot_to_base64(plt)
    assert base64_image is not None
