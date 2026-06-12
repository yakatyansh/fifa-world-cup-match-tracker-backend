from datetime import datetime
from zoneinfo import ZoneInfo


def convert_to_ist(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%m/%d/%Y %H:%M")

        # Replace with the actual source timezone
        dt = dt.replace(tzinfo=ZoneInfo("America/Mexico_City"))

        ist_dt = dt.astimezone(ZoneInfo("Asia/Kolkata"))

        return ist_dt.isoformat()

    except Exception:
        return date_str