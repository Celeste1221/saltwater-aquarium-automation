# Saltwater Aquarium Monitoring & Automation with Raspberry Pi

A modular, lower-cost prototype for monitoring reef aquarium conditions and exploring remote equipment control. The project combines **Raspberry Pi, Python, GPIO-connected sensors, custom circuitry, Adafruit IO**, and a separate experimental **CircuitPython** actuator controller.

> **Portfolio status:** This is a historical engineering prototype, **not** a production-ready or fail-safe aquarium controller. 

## Why it matters
Reef aquariums rely on stable water conditions. Monitoring, trending, alerting, and reliable automation can reduce routine effort and help identify environmental changes. This project investigated a customizable alternative to commercial controllers such as Neptune Apex and CoralVue Hydros.


## What the field project demonstrated
- DS18B20 temperature sensor readings and a Python-to-Adafruit IO data pipeline.
- Optical water-level monitoring and publishing to an Adafruit IO feed.
- Construction of modular electronics for a relay-based power controller and sensor interfaces.
- Remote equipment-control functionality reported in the thesis, including timed operations (complete Raspberry Pi control code not yet recovered).
- Comparison of DIY construction with commercial and semi-DIY controller configurations.
- Exploration of a separate CircuitPython HTTP actuator controller (not yet hardware-validated).

## Technology
`Python` · `Raspberry Pi` · `DS18B20` · `gpiozero` · `Adafruit IO` · `REST` · `CircuitPython` · `GPIO` · `electronics prototyping`

## Deployment caution
**Do not connect this code directly to life-support equipment.** Relay outputs, power switching, sensor polarity, failure modes, access control, and electrical isolation need bench testing, independent safety protections, and supervision. CircuitPython and Raspberry Pi scripts target different runtimes and are not interchangeable.

## Run the Raspberry Pi sensor examples (after hardware verification)
1. Use Raspberry Pi OS and enable the 1-Wire interface for DS18B20.
2. Create a virtual environment and install `pip install -r requirements.txt` plus `gpiozero` for the water-level example.
3. Create Adafruit IO feeds `temperature` and `water-level`.
4. Set `ADAFRUIT_IO_USERNAME` and `ADAFRUIT_IO_KEY` as environment variables (see `.env.example`, which is **not** loaded automatically).
5. From `src/raspberry_pi`, run `python temperature_to_adafruit_io.py` or `python water_level_to_adafruit_io.py` after verifying GPIO and electrical connections.

## Development timeline / next steps
- **Completed/documented:** modular circuit assembly, sensor integration and real-time dashboard demonstrations, cost comparison and report.
- **Future development:** improved error handling, verified relay control, integration tests, pH/salinity sensing, improved user interface, alerts and fail-safe automation.

## Project cost
The thesis reports an actual project expenditure of **$419.46**, reflecting expedited purchases and extra components. This is a historical **2025 project cost**, not a current parts quote or a like-for-like commercial feature comparison.

## Original documentation
- [Hardware guides from Adafruit / reef-pi](https://learn.adafruit.com/reef-pi-power-controller)

## Attribution
The circuit designs drew on open-source **reef-pi** / Adafruit Learning System guides. This repository contains the author's adapted scripts and project notes, not a re-publication of reef-pi itself. Some thesis sensor parsing logic was adapted from a community snippet credited in the thesis. See the original report for full references.
