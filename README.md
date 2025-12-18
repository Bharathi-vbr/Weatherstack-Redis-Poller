# Weatherstack Redis Poller

Small Weatherstack + Redis polling service 

---

## 1. Requirements

- Python 3  
- Redis running locally (`localhost:6379`)  
- Weatherstack API key from <https://weatherstack.com> 

---

## 2. Setup
```bash
git clone <this-repo-url>
cd Weatherstack Redis Poller
```
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install --upgrade pip
pip install redis requests
```
---

## 3. Configure

Set environment variables:
```bash
export WEATHERSTACK_API_KEY=YOUR_API_KEY
export WEATHER_LOCATIONS="New York, USA;Dallas, USA"
export POLL_INTERVAL_SECONDS=10 # optional, default 60
```

`config.py` reads these and sets Redis host/port/DB, cache TTL, and locations. 

---

## 4. Run

python main.py

```bash

You will see logs like:

[INFO] Starting poller...
[INFO] Calling Weatherstack for New York, USA
[INFO] Redis GET weather:New York, USA -> MISS
[INFO] Redis SETEX weather:New York, USA ttl=600
[INFO] Sleeping 10 seconds before next poll

```

---

## 5. What the code shows
```bash
- Periodic API polling for all configured locations. 
- Redis `GET`, `SETEX` (create with TTL), and update (upsert). 
- Clear logging around each poll and Redis operation for easy explanation in the interview. 
```
