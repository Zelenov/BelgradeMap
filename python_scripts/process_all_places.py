#!/usr/bin/env python3
"""
Process All Places - Batch processor for Belgrade Instagram places

This script reads all Instagram URLs from map.md and runs the MapCreator make_place script
for each place to create organized folder structures with parsed data.

Usage:
    python process_all_places.py
"""

import os
import sys
import subprocess
from pathlib import Path

def read_instagram_urls(map_file_path):
    """
    Read Instagram URLs from the map.md file.
    
    Args:
        map_file_path (str): Path to the map.md file
        
    Returns:
        list: List of Instagram URLs
    """
    urls = []
    try:
        with open(map_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and line.startswith('https://www.instagram.com/'):
                    urls.append(line)
        return urls
    except FileNotFoundError:
        print(f"❌ Error: Could not find {map_file_path}")
        return []
    except Exception as e:
        print(f"❌ Error reading {map_file_path}: {e}")
        return []

def run_make_place(instagram_url, output_folder):
    """
    Run the MapCreator make_place script for a single Instagram URL.
    
    Args:
        instagram_url (str): Instagram URL to process
        output_folder (str): Output folder for the place data
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Path to the make_place script
    script_path = Path(__file__).parent.parent.parent / "MapCreator" / "src" / "make_place" / "make_place.py"
    
    if not script_path.exists():
        print(f"❌ Error: Could not find make_place script at {script_path}")
        return False
    
    try:
        # Run the make_place script with UTF-8 encoding
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        cmd = [
            sys.executable,
            str(script_path),
            '-i', instagram_url,
            '-o', output_folder
        ]
        
        print(f"🔄 Processing: {instagram_url}")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=script_path.parent, env=env, encoding='utf-8')
        
        if result.returncode == 0:
            print(f"✅ Successfully processed: {instagram_url}")
            return True
        else:
            print(f"❌ Failed to process {instagram_url}")
            print(f"   Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Exception while processing {instagram_url}: {e}")
        return False

def main():
    """Main function to process all places."""
    print("🏗️  Process All Places - Belgrade Instagram Places Batch Processor")
    print("=" * 70)
    
    # Get the current script directory and find map.md
    script_dir = Path(__file__).parent
    belgrade_map_dir = script_dir.parent
    map_file_path = belgrade_map_dir / "map.md"
    
    # Read Instagram URLs
    print(f"📄 Reading Instagram URLs from: {map_file_path}")
    urls = read_instagram_urls(map_file_path)
    
    if not urls:
        print("❌ No Instagram URLs found in map.md")
        return
    
    print(f"📊 Found {len(urls)} Instagram URLs to process")
    
    # Create output folder
    output_folder = belgrade_map_dir / "maps" / "belgrade"
    output_folder.mkdir(parents=True, exist_ok=True)
    print(f"📁 Output folder: {output_folder}")
    
    # Process each URL
    successful = 0
    failed = 0
    
    print("\n🔄 Starting batch processing...")
    print("-" * 50)
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")
        
        if run_make_place(url, str(output_folder)):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 70)
    print("🎉 BATCH PROCESSING COMPLETE!")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {len(urls)}")
    print(f"📁 Output location: {output_folder}")

if __name__ == "__main__":
    main()
