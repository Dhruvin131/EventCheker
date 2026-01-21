
from collections import deque
from fastapi.routing import APIRouter

router = APIRouter()

from pydantic import BaseModel

class EventsRequest(BaseModel):
    lsEvents: list[int]

@router.post("/events")
def isLimitExceed(eventReq: EventsRequest) -> bool:
    """
    Function to check if the number of events exceeds the limit of 100 within 60 seconds.
    
    Args:
    lsEvents (list): List of events.
    
    Returns:
    bool: True if the number of events exceeds 100 within 60 seconds, False otherwise.
    """
    lsEvents = eventReq.lsEvents
    try:
        lsEvents = sorted([int(i) for i in lsEvents])
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
    
    window = deque()
    for j in lsEvents:
        window.append(j)
        while window and j-window[0] > 60:
            window.popleft()
        if len(window) > 100:
            return True
        
    return False

if __name__ == "__main__":
    pass