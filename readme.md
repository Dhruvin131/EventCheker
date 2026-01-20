# Eventchecker
An eventchecker that checks for events and returns True when even exceeds specified time limit.

# Feature
- Check for Events from event stream
- Unittest using pytest

# Installation
pip install -r requirements.txt

# Usage Example
Run the Service using following command
` Uvicorn app.main:app --reload `

```
Method type: Post
Route: /events
Body: lsEvents:[int, int, int....]
```
and now you can call the post api using `localhost:port/events` with events body as list of integers to call the route

