# BelgradeMap Python Scripts

This folder contains Python scripts for processing Belgrade Instagram places.

## Scripts

### process_all_places.py

A simple batch processor that reads all Instagram URLs from `map.md` and runs the MapCreator make_place script for each place.

**Usage:**
```bash
cd BelgradeMap/python_scripts
python process_all_places.py
```

**What it does:**
1. Reads all Instagram URLs from `../map.md`
2. For each URL, runs `MapCreator/src/make_place/make_place.py`
3. Creates organized folder structures in `../maps/belgrade/`
4. Shows progress and summary of successful/failed processing

**Requirements:**
- Python 3.6+
- MapCreator scripts must be available in the parent directory structure
- No additional Python packages required (uses only standard library)

**Output:**
- Creates folders for each Instagram place in `../maps/belgrade/`
- Each folder contains `README.md` and `place_data.json` with parsed information
