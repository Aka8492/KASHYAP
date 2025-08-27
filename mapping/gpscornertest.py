import csv
import geocoder

with open("corners.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Corner No", "Latitude", "Longitude"])
    corner_count = 1

    print("Move to a corner (physically or simulate) and press Enter to save GPS coordinate.")
    try:
        while True:
            # Get laptop location (via IP/WiFi)
            g = geocoder.ip('me')
            lat, lon = g.latlng if g.ok else (None, None)

            if lat and lon:
                print(f"Current Position: LAT={lat:.6f}, LNG={lon:.6f}", end="\r")

                # Wait for user input to save as corner
                if input() == "":
                    writer.writerow([corner_count, lat, lon])
                    file.flush()
                    print(f"\n✅ Corner {corner_count} saved: {lat:.6f}, {lon:.6f}")
                    corner_count += 1
                    if corner_count > 4:  # only 4 corners
                        print("All 4 corners recorded. Exiting.")
                        break
            else:
                print("⚠️ Could not fetch location. Check internet/GPS settings.")
    except KeyboardInterrupt:
        print("\nStopped.")
