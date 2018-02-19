#!/usr/bin/env python3

import json
from pathlib import Path


DATA_SCHEMA = {
    "transformed_data": {
        "values_low": [],
        "values_high": []
    }
}

IN_FILE = 'data.json'
STAGE_ONE_OUT_FILE = 'stage_one_data_out.json'
STAGE_TWO_OUT_FILE = 'stage_two_data_out.json'


def stage_one():
    """Stage 1 Processing
    """
    stage_one_data = json.loads(Path(IN_FILE).read_text())
    
    data_low = [50*int(num) for num in stage_one_data["transformed_data"]['values_low']]
    data_high = [100*num for num in data_low]

    DATA_SCHEMA["transformed_data"]['values_low'] = data_low
    DATA_SCHEMA["transformed_data"]['values_high'] = data_high
    Path(STAGE_ONE_OUT_FILE).write_text(json.dumps(DATA_SCHEMA))


def stage_two():
    """Stage 2 Processing
    """
    stage_two_data = json.loads(Path(STAGE_ONE_OUT_FILE).read_text())

    data_low = [50*int(num) for num in stage_two_data["transformed_data"]['values_low']]
    data_high = [100*num for num in data_low]

    DATA_SCHEMA["transformed_data"]['values_low'] = data_low
    DATA_SCHEMA["transformed_data"]['values_high'] = data_high
    Path(STAGE_TWO_OUT_FILE).write_text(json.dumps(DATA_SCHEMA))


def pipeline():
    stage_one()
    stage_two()


if __name__ == "__main__":
    pipeline()
