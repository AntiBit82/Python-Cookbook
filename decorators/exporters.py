from typing import Callable
from functools import wraps

type Data = dict[str, str]
type ExporterFn = Callable[[Data], None]

_exporters: dict[str, ExporterFn] = {}


def register_exporter(name: str, times: int = 1) -> Callable[[ExporterFn], ExporterFn]:
    def decorator(fn: ExporterFn) -> ExporterFn:
        @wraps(fn)
        def wrapper(data: Data):
            for i, _ in enumerate(range(times)):
                print(f"Exporter '{name}' - pass {i + 1} of {times}")
                fn(data)

        _exporters[name] = wrapper
        return wrapper
    return decorator


@register_exporter("csv", times=2)  # same as: export_csv = register_exporter("csv")(export_csv) 
def export_csv(data: Data):
    print(f"Exporting data as CSV: {data}")


@register_exporter("json")
def export_json(data: Data):
    print(f"Exporting data as JSON: {data}")


@register_exporter("xml")
def export_xml(data: Data):
    print(f"Exporting data as XML: {data}")


def export_data(format: str, data: Data):
    exporter = _exporters.get(format)
    if not exporter:
        raise ValueError(f"Exporter for format '{format}' not found.")
    exporter(data)


if __name__ == "__main__":
    print("Available exporters:", list(_exporters))
    sample_data = {"name": "Alice", "age": "30", "city": "Wonderland"}

    export_data("csv", sample_data)
    export_data("json", sample_data)
