# Fellow Aiden

[![PyPI version](https://badge.fury.io/py/fellow-aiden.svg)](https://badge.fury.io/py/fellow-aiden)

This library provides an interface to the Fellow Aiden coffee brewer.

## Quick Start

**Install the library**:

```sh
pip install fellow-aiden
# or
python setup.py install
```

**Set ENV variables**:

```sh
export FELLOW_EMAIL='YOUR-EMAIL-HERE'
export FELLOW_PASSWORD='YOUR-PASSWORD-HERE'
```

## Sample Code

This sample code shows some of the range of functionality within the library:

```python
import os
from fellow_aiden import FellowAiden

# EMAIL = "YOUR-EMAIL-HERE"
# PASSWORD = "YOUR-PASSWORD-HERE"

EMAIL = os.environ['FELLOW_EMAIL']
PASSWORD = os.environ['FELLOW_PASSWORD']

# Create an instance
aiden = FellowAiden(EMAIL, PASSWORD)

# Get device settings
aiden.get_settings()

# Get display name of brewer
aiden.get_display_name()

# Get profiles
aiden.get_profiles()

# Add a profile
profile = {
    "profileType": 0,
    "title": "Debug-FellowAiden",
    "ratio": 16,
    "bloomEnabled": True,
    "bloomRatio": 2,
    "bloomDuration": 30,
    "bloomTemperature": 96,
    "ssPulsesEnabled": True,
    "ssPulsesNumber": 3,
    "ssPulsesInterval": 23,
    "ssPulseTemperatures": [96,97,98],
    "batchPulsesEnabled": True,
    "batchPulsesNumber": 2,
    "batchPulsesInterval": 30,
    "batchPulseTemperatures": [96,97]
}
aiden.create_profile(profile)

# Delete a profile
aiden.delete_profile_by_id('p1')

# Add profile from shared brew link
aiden.create_profile_from_link('https://brew.link/p/ws98')
```

## Profile Details

Below is an example profile:

```json
[{
    "id": "p0",
    "profileType": 0,
    "title": "Hot Water",
    "ratio": 15,
    "bloomRatio": null,
    "bloomDuration": null,
    "bloomTemperature": null,
    "ssPulsesNumber": 1,
    "ssPulsesInterval": 1,
    "ssPulseTemperatures": [99],
    "batchPulsesNumber": 1,
    "batchPulsesInterval": 5,
    "batchPulseTemperatures": [99],
    "overallTemperature": null,
    "isDefaultProfile": false,
    "bloomEnabled": false,
    "instantBrew": false,
    "folder": "Custom",
    "duration": null,
    "lastGBQuantity": null,
    "lastUsedTime": null,
    "deviceId": "FB_02c4139a-50c6-f4ce-363b-6f9e1840307e",
    "ssPulsesEnabled": true,
    "batchPulsesEnabled": true,
    "synced": true
}]
```

## Features

* Access all settings and details from Aiden brewer
* Manage custom brewing profiles
* Add shared profiles from URL
