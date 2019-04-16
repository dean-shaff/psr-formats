### psr-formats

Formats for loading and saving data using in pulsar data processing.

Supported formats:
  - DADA

### Usage

```python
from psr_formats import DADAFile

dada_file = DADAFile("path/to/dada.dump")
dada_file.load_data()

dada_file["NCHAN"]
dada_file.nchan
dada_file["NPOL"]
dada_file.npol

dada_file.data.shape
```

### Testing

```
poetry run python -m unittest
```
