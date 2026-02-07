# airline-tracker

A tiny CLI utility I use to sanity-check flight telemetry + basic gate/turn events for ops notes.
Not production-grade, just quick tooling.

## Features
- Reads a sample flight telemetry JSON feed (altitude/speed/lat/lon)
- Reads a CSV of “ops events” (gate in/out, delays, holds)
- Prints a quick summary and flags anomalies

## Usage
```bash
pip install -r requirements.txt
python tracker.py
