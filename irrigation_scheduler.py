def parse_irrigation_schedule(schedule_str):
    if schedule_str is None:
        raise TypeError("Schedule string cannot be None")
    if not isinstance(schedule_str, str):
        raise TypeError("Schedule input must be a string")
    if schedule_str.strip() == "":
        return []
        
    parts = schedule_str.split(',')
    schedule = []
    for part in parts:
        part = part.strip()
        if part == "":
            raise ValueError("Empty interval found in schedule string")
        val = int(part)
        if val < 0:
            raise ValueError("Irrigation duration cannot be negative")
        schedule.append(val)
    return schedule

def calculate_total_water(durations, flow_rate):
    if durations is None or flow_rate is None:
        raise TypeError("Inputs cannot be None")
    if not isinstance(durations, list):
        raise TypeError("Durations must be a list")
    if not isinstance(flow_rate, (int, float)):
        raise TypeError("Flow rate must be a number")
    if flow_rate < 0:
        raise ValueError("Flow rate cannot be negative")
        
    total_duration = 0
    for d in durations:
        if not isinstance(d, (int, float)):
            raise TypeError("Duration items must be numbers")
        if d < 0:
            raise ValueError("Duration item cannot be negative")
        total_duration += d
        
    return total_duration * flow_rate

if __name__ == "__main__":
    print("Running Irrigation Scheduler application...")
    try:
        print("Parsed schedule ('10, 20, 30'):", parse_irrigation_schedule("10, 20, 30"))
        print("Total water (durations=[10, 20], rate=5.0):", calculate_total_water([10, 20], 5.0))
    except Exception as e:
        print(f"Error: {e}")