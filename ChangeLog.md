### v0.1.0

- Took format files from `pfb` repo.
- Updated tests to reflect new default values in `DADAFile` methods.

### v0.1.1

- Added `timestamp_formatter` class attribute
- Added `utc_start` property to `DADAFile` class. The getter returns a
`datetime.datetime` object, and the setter can take a `str` or a
`datetime.datetime` object.
- Added corresponding test for `DADAFile` class.

### v0.2.0

TODO:
- Need to update tests to use significantly smaller test data files so
tests can run in CI environment.
- Need to create separate `DataFile` unittest, that steals some of the
functionality the `DADAFile` test.
