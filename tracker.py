import json
import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

def load_flights(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_events(path: Path):
    events = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            events.append(row)
    return events

def summarize_flight(points):
    altitudes = [p["alt_ft"] for p in points]
    speeds = [p["gs_kt"] for p in points]
    return {
        "samples": len(points),
        "alt_min": min(altitudes),
        "alt_max": max(altitudes),
        "alt_avg": round(mean(altitudes), 1),
        "gs_min": min(speeds),
        "gs_max": max(speeds),
        "gs_avg": round(mean(speeds), 1),
    }

def main():
    flights = load_flights(DATA / "sample_flights.json")
    events = load_events(DATA / "sample_events.csv")

    print("=== Airline Tracker (demo) ===")
    print(f"Flights loaded: {len(flights)}")
    print(f"Events loaded: {len(events)}\n")

    for flt in flights:
        fid = flt["flight_id"]
        summary = summarize_flight(flt["telemetry"])
        print(f"[{fid}] samples={summary['samples']} alt(avg/min/max)={summary['alt_avg']}/{summary['alt_min']}/{summary['alt_max']} "
              f"gs(avg/min/max)={summary['gs_avg']}/{summary['gs_min']}/{summary['gs_max']}")

        # tiny “anomaly” check
        if summary["alt_max"] - summary["alt_min"] > 8000:
            print("  ! altitude swing looks large (possible step climb or bad data)")

    print("\n=== Recent Ops Events ===")
    for e in events[-5:]:
        print(f"{e['ts']}  {e['airport']}  {e['event']}  {e['flight']}  {e['note']}")

if __name__ == "__main__":
    main()
