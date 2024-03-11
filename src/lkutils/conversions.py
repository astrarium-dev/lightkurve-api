from io import BytesIO
import base64


def convert_plot_to_base64(plt) -> str:
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode plot bytes to base64 string
    plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return plot_base64


def convert_plot_to_bytes(plt) -> bytes:
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return buffer.getvalue()
