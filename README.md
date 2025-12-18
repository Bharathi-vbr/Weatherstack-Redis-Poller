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
- Periodic API polling for all configured locations. 
- Redis `GET`, `SETEX` (create with TTL), and update (upsert). 
- Clear logging around each poll and Redis operation for easy explanation in the interview. 

## 6. How this could be operationalized

This code is already split into small, reusable pieces: `weather_client.py` (API client), `redis_client.py` (cache client), `config.py` (configuration), and `main.py` (orchestration loop).That makes it easy to drop into a larger system or reuse the clients in other jobs.

**If turning this into a production-style service, some next steps would be:**

- Containerize it (e.g., Docker) and pass all configuration through environment variables, so the same image can run in dev/staging/prod.
- Run it under a scheduler/orchestrator (systemd timer, Kubernetes Deployment or CronJob) to control frequency and rollout.
- Add basic observability: metrics (poll success/failure, cache hits/misses) and structured logs for easy debugging.
- Add a few small unit tests for configuration and Redis key/TTL behavior to make it safer to reuse and extend.

