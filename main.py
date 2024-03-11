# Import necessary libraries
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import lightkurve as lk
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define API endpoint for generating lightkurve plots
@app.post('/generate_lightcurve_plot')
async def generate_lightcurve_plot(request: Request):
    # Parse request JSON data
    request_data = await request.json()
    target = request_data.get('target')

    try:
        # Fetch the light curve data using Lightkurve
        lc = lk.search_lightcurve(target=target, mission="Kepler").download().PDCSAP_FLUX
        # Plot the light curve
        lc.plot()
        plt.xlabel("Time (days)")
        plt.ylabel("Flux")
        plt.title("Light Curve")

        plot_base64 = convert_plot_to_base64(plt)
        # Return the base64 encoded plot
        return JSONResponse(content=jsonable_encoder({'plot': plot_base64}), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def convert_plot_to_base64(plt) -> str:
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode plot bytes to base64 string
    plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return plot_base64


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
