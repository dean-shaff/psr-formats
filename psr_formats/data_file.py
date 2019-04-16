# data_file.py
import logging
import typing

import numpy as np


module_logger = logging.getLogger(__name__)

__all__ = [
    "DataFile",
]


class DataFile:

    def __init__(self, file_path: str):
        self.logger = module_logger.getChild("DataFile")
        self._file_path = file_path
        self._header = None
        self._data = None

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        self._file_path = file_path
        self._data = None
        self._header = None

    @property
    def header(self) -> dict:
        return self._header

    @header.setter
    def header(self, new_header: dict) -> None:
        self._header = new_header.copy()

    @property
    def data(self) -> np.ndarray:
        return self._data

    @data.setter
    def data(self, new_data: np.ndarray):
        # if new_data.ndim != 1 and new_data.ndim != 4:
        #     raise RuntimeError(f"Ambiguous data shape: {new_data.ndim}")
        iscomplex = np.iscomplexobj(new_data)
        ndim = 2 if iscomplex else 1
        ndat = new_data.shape[0]

        if new_data.ndim == 1:
            nchan, npol = 1, 1
            self._data = np.zeros((ndat, nchan, npol), dtype=new_data.dtype)
            self._data[:, 0, 0] = new_data
        else:
            nchan, npol = new_data.shape[1], new_data.shape[2]
            self._data = new_data

        self["NDAT"] = str(ndat)
        self["NCHAN"] = str(nchan)
        self["NPOL"] = str(npol)
        self["NDIM"] = str(ndim)

    @property
    def nchan(self) -> int:
        return int(self["NCHAN"])

    @property
    def ndim(self) -> int:
        return int(self["NDIM"])

    @property
    def npol(self) -> int:
        return int(self["NPOL"])

    @property
    def ndat(self) -> int:
        if self.data is not None:
            if self.data.ndim > 1:
                return self.data.shape[0]

    def __getitem__(self, item: str) -> typing.Any:
        if self._header is not None:
            if item in self._header:
                return self._header[item]

    def __setitem__(self, item: str, val: typing.Any) -> None:
        if self._header is not None:
            if item in self._header:
                self._header[item] = val

    def __contains__(self, item: str) -> bool:
        if self._header is not None:
            if item in self._header:
                return True
            else:
                return False
        else:
            raise RuntimeError(("DataFile.__contains__: Need to load "
                                "data from file before calling __contains__"))

    def load_data(self):
        raise NotImplementedError()

    def dump_data(self, overwrite=False):
        raise NotImplementedError()
