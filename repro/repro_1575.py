"""Repro for ecmwf/WeatherGenerator#1575: write the same output item twice."""
import pathlib
import tempfile

from weathergen.common.io import ItemKey, OutputItem, zarrio_writer

store = pathlib.Path(tempfile.mkdtemp()) / "out.zarr"
key = ItemKey(sample=0, forecast_step=1, stream="ERA5")
item = OutputItem(key=key, forecast_offset=None)

with zarrio_writer(store) as zio:
    zio.write_zarr(item)
    print("first write ok:", key.path)
    try:
        zio.write_zarr(item)
        print("second write: no error")
    except Exception as e:
        print(f"second write raised {type(e).__name__}: {e}")
print("python -O active:", not __debug__)