# lambdata-dougscohen

## Installation

```sh
pip install -i https://test.pypi.org/simple/ lambdata-dougscohen
```
## Contents

function `convert_to_seconds()` where you input a time in the format
"minutes:seconds" and converts the time to seconds as an integer.

function `state_abbrev()` where you input a full state name and the function
chnages it to its abbreviation.

## Usage

```py
from my_lambdata.my_mod import convert_to_seconds, state_abbrev

print(convert_to_seconds('1:14'))
print(state_abbrev('North Dakota'))
```